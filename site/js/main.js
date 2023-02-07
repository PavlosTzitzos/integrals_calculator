KasperskyLab.AddRunner("vk", (ns, session, settings, locales) =>
{
function VirtualKeyboard()
{
    const ProtectState = { NOT_PROTECTED: 0, STARTING_PROTECT: 1, PROTECTED: 2, STOPPING_PROTECT: 3 };
    const m_unsupportedLayouts = [
        "00000411", 
        "00000804", 
        "00000404", 
        "00000c04", 
        "00001404", 
        "00001004"
    ];

    let m_callFunction = () => {};
    let m_virtualKeyboardIconShowMode = 0;
    let m_secureInputProtectMode = 0;

    let m_activeElement = null;
    let m_lastFocusedElement = null;
    let m_protectedState = ProtectState.NOT_PROTECTED;
    let m_enabledSecureInput = false;
    let m_protectChangeTimeout = null;
    let m_protectableSecureInputChecker = null;
    let m_protectableVirtualKeyboardIconChecker = null;
    let m_protectedText = null;
    let m_postponeStart = null;
    let m_ready = false;
    let m_isUnsupportedLayout = false;

    function ShowVirtualKeyboard()
    {
        if (m_lastFocusedElement)
            m_lastFocusedElement.focus();
        m_callFunction("vk.showKeyboard");
    }

    const m_tooltip = new ns.SecureInputTooltip(locales, session);
    const m_icon = new ns.VirtualKeyboardInputIcon(ShowVirtualKeyboard, session);
    const m_protectableVirtualKeyboardChecker = new ns.ProtectableElementDetector(settings.vkProtectMode);
    let m_observer = null;

    function OnPing()
    {
        return (m_protectedState === ProtectState.STARTING_PROTECT || m_protectedState === ProtectState.PROTECTED) ? 500 : ns.MaxRequestDelay;
    }

    function OnError()
    {
        m_ready = false;
        m_protectedState = ProtectState.NOT_PROTECTED;
    }
    function SetSettings(argument)
    {
        SetSettingsImpl(argument.virtualKeyboardIconShowMode, argument.secureInputProtectMode);
    }
    function SetSettingsImpl(newVirtualKeyboardIconShowMode, newSecureInputProtectMode)
    {
        if (newSecureInputProtectMode !== m_secureInputProtectMode)
            m_protectableSecureInputChecker = new ns.ProtectableElementDetector(newSecureInputProtectMode);
        if (newVirtualKeyboardIconShowMode !== m_virtualKeyboardIconShowMode)
            m_protectableVirtualKeyboardIconChecker = new ns.ProtectableElementDetector(newVirtualKeyboardIconShowMode);
        const needToUpdate = (newSecureInputProtectMode > m_secureInputProtectMode
            || newVirtualKeyboardIconShowMode > m_virtualKeyboardIconShowMode);

        m_secureInputProtectMode = newSecureInputProtectMode;
        m_virtualKeyboardIconShowMode = newVirtualKeyboardIconShowMode;

        if (needToUpdate && m_observer)
            m_observer.settingsChanged();
    }

    function InsertCharacter(character)
    {
        const start = m_activeElement.selectionStart;
        const end = m_activeElement.selectionEnd;
        m_activeElement.value = m_activeElement.value.substring(0, start) + character + m_activeElement.value.substring(end);
        m_activeElement.setSelectionRange(start + character.length, start + character.length);
        m_protectedText = m_activeElement.value;
    }

    function CheckPasswordLength(character)
    {
        if (m_activeElement.maxLength && m_activeElement.maxLength > 0)
            return (m_activeElement.value.length + character.length) <= m_activeElement.maxLength;
        return true;
    }

    function GenerateKeyboardEvent(eventName, key, scanCodeValue, virtualCode, shiftKey)
    {
        const keyboardEventOptions = { key: key, keyCode: virtualCode, code: scanCodeValue, bubbles: true, shiftKey: shiftKey, cancelable: true, which: virtualCode };
        if (eventName === "keypress")
            keyboardEventOptions.charCode = virtualCode;
        const keyboardEvent = new KeyboardEvent(eventName, keyboardEventOptions);
        return m_activeElement.dispatchEvent(keyboardEvent);
    }

    function GenerateInputEvent(eventName, data)
    {
        const inputEvent = new InputEvent(eventName, { data: data, bubbles: true, inputType: "insertText", cancelable: true });
        return m_activeElement.dispatchEvent(inputEvent);
    }

    function GenerateChangeEvent()
    {
        m_protectedText = null;
        const changeEvent = new Event("change", { bubbles: true });
        m_activeElement.dispatchEvent(changeEvent);
    }
    function KeyDown(keyInfo)
    {
        ns.SessionLog("Key down process");
        if (!m_activeElement)
        {
            ns.SessionLog("Key down skip. No active element");
            return;
        }
        const key = (keyInfo.isDeadKey) ? "Dead" : String.fromCharCode(keyInfo.symbols[0]);
        if (GenerateKeyboardEvent("keydown", key, keyInfo.scanCodeValue, keyInfo.virtualCode, keyInfo.shift) === false)
            return;

        for (let symbolIndex = 0; symbolIndex < keyInfo.symbols.length; ++symbolIndex)
        {
            const character = String.fromCharCode(keyInfo.symbols[symbolIndex]);
            if (GenerateKeyboardEvent("keypress", character, keyInfo.scanCodeValue, keyInfo.symbols[symbolIndex], keyInfo.shift) === false)
                continue;
            if (GenerateInputEvent("beforeinput", character) === false)
                continue;
            if (!CheckPasswordLength(character))
                break;

            InsertCharacter(character);
            GenerateInputEvent("input", character);
        }
    }

    function KeyUp(keyInfo)
    {
        ns.SessionLog("Key up process");
        if (!m_activeElement)
        {
            ns.SessionLog("Key up skip. No active element");
            return;
        }

        const key = (keyInfo.isDeadKey) ? "Dead" : String.fromCharCode(keyInfo.symbols[0]);
        GenerateKeyboardEvent("keyup", key, keyInfo.scanCodeValue, keyInfo.virtualCode, keyInfo.shift);
    }

    function GetKeyboardLayout(keyboardLayoutInfo)
    {
        if (m_unsupportedLayouts.includes(keyboardLayoutInfo.layout))
        {
            ns.SessionLog("Layout is unsupported");
            m_isUnsupportedLayout = true;
            if (m_activeElement && (m_protectedState === ProtectState.STARTING_PROTECT || m_protectedState === ProtectState.PROTECTED))
                StopProtect();
        }
        else
        {
            m_isUnsupportedLayout = false;
            if (m_activeElement && NeedProtectElement(m_activeElement)
                && (m_protectedState === ProtectState.NOT_PROTECTED || m_protectedState === ProtectState.STOPPING_PROTECT))
                StartProtect();
        }
    }

    function OnDocumentKeyUp(event)
    {
        m_callFunction("nms", "CheckKeyboardLayout");

        if (m_activeElement === event.target && event.keyCode === 13 && m_protectedText === m_activeElement.value)
            GenerateChangeEvent();
    }
    function NeedProtectElement(element)
    {
        return m_protectableSecureInputChecker.Test(element) || m_protectableVirtualKeyboardChecker.Test(element);
    }
    function HandleStartProtectCallback(result, args, needSecureInputCall)
    {
        if (m_protectedState === ProtectState.STOPPING_PROTECT)
        {
            if (result === 0)
                StopProtect();
            else
                m_protectedState = ProtectState.NOT_PROTECTED;
            return;
        }
        if (result === 0)
        {
            if (!args)
            {
                ns.SessionLog("ERR VK - unexpected arguments");
                return;
            }
            m_enabledSecureInput = args.isSecureInput;
            m_protectedState = ProtectState.PROTECTED;
            const needSecureInput = m_protectableSecureInputChecker.Test(m_activeElement);
            if (needSecureInput === needSecureInputCall)
                ShowBalloons();
            else
                CheckProtectModeAndShowBalloons();
            return;
        }
        else if (result === 1)
        {
            m_postponeStart = ns.SetTimeout(() => { OnElementFocus(m_activeElement); }, 100);
        }
        m_protectedState = ProtectState.NOT_PROTECTED;
    }

    function StartProtect()
    {
        if (!document.hasFocus())
        {
            m_protectedState = ProtectState.NOT_PROTECTED;
            ns.SessionLog("No focus on StartProtect");
            return;
        }
        const needSecureInput = m_protectableSecureInputChecker.Test(m_activeElement);
        m_protectedState = ProtectState.STARTING_PROTECT;
        m_callFunction("vk.startProtect", { isSecureInput: needSecureInput }, (result, args) => { HandleStartProtectCallback(result, args, needSecureInput); });
    }
    function ChangeMode()
    {
        const needSecureInput = m_protectableSecureInputChecker.Test(m_activeElement);
        m_protectedState = ProtectState.STARTING_PROTECT;
        m_callFunction("vk.changeMode", { isSecureInput: needSecureInput }, (result, args) => { HandleStartProtectCallback(result, args, needSecureInput); });
    }

    function StopProtect()
    {
        m_protectedState = ProtectState.STOPPING_PROTECT;
        m_callFunction("vk.stopProtect", null, result =>
            {
                if (m_protectedState === ProtectState.STARTING_PROTECT && result === 0)
                {
                    StartProtect();
                    return;
                }

                m_protectedState = ProtectState.NOT_PROTECTED;
                m_icon.Hide();
                m_tooltip.Hide();
            });
    }

    function ShowBalloons()
    {
        if (m_enabledSecureInput)
            m_tooltip.Show(m_activeElement);
        if (m_protectableVirtualKeyboardIconChecker.Test(m_activeElement))
            m_icon.Show(m_activeElement);
    }

    function CheckProtectModeAndShowBalloons()
    {
        const needSecureInput = m_protectableSecureInputChecker.Test(m_activeElement);
        if (needSecureInput !== m_enabledSecureInput)
            ChangeMode();
        else
            ShowBalloons();
    }

    function OnElementFocus(element)
    {
        if (!m_ready)
            return;

        m_activeElement = element;
        m_lastFocusedElement = element;

        if (!NeedProtectElement(element))
            return;

        ns.ProtectableElementDetector.ChangeTypeIfNeeded(element);

        clearTimeout(m_postponeStart);
        clearTimeout(m_protectChangeTimeout);
        m_protectChangeTimeout = ns.SetTimeout(() => { ProcessFocus(element); }, 0);
    }

    function OnElementBlur(element)
    {
        if (!m_ready)
            return;

        if (m_activeElement === element && m_protectedText === m_activeElement.value)
            GenerateChangeEvent();
        clearTimeout(m_postponeStart);
        m_icon.Hide();
        m_tooltip.Hide();

        ns.ProtectableElementDetector.RestoreTypeIfNeeded(element);

        clearTimeout(m_protectChangeTimeout);
        m_protectChangeTimeout = ns.SetTimeout(() => { ProcessBlur(); }, 0);
        m_activeElement = null;
    }

    function OnSettingsChanged(element)
    {
        const needProtectElement = NeedProtectElement(element);
        if ((m_activeElement !== element) ^ needProtectElement)
            return;

        if (needProtectElement)
            OnElementFocus(element);
        else
            OnElementBlur(element);
    }

    function ProcessFocus(element)
    {
        if (m_protectedState === ProtectState.NOT_PROTECTED && !m_isUnsupportedLayout)
        {
            if (element === document.activeElement)
                StartProtect();
            else
                ns.SessionLog("Focused element is not active");
        }
        else if (m_protectedState === ProtectState.PROTECTED)
        {
            CheckProtectModeAndShowBalloons();
        }
        else if (m_protectedState === ProtectState.STOPPING_PROTECT)
        {
            m_protectedState = ProtectState.STARTING_PROTECT;
        }
    }

    function ProcessBlur()
    {
        if (m_protectedState === ProtectState.PROTECTED)
            StopProtect();
        else if (m_protectedState === ProtectState.STARTING_PROTECT)
            m_protectedState = ProtectState.STOPPING_PROTECT;
    }

    function Init()
    {
        session.InitializePlugin((activatePlugin, registerMethod, callFunction) =>
        {
            m_callFunction = callFunction;
            activatePlugin("vk", OnPing, OnError);
            registerMethod("vk.settings", SetSettings);
            registerMethod("vk.keyDown", KeyDown);
            registerMethod("vk.keyUp", KeyUp);
            registerMethod("vk.keyboardLayout", GetKeyboardLayout);
            ns.AddEventListener(document, "keyup", OnDocumentKeyUp);
            ns.AddEventListener(document, "mouseenter", OnDocumentKeyUp);
            m_ready = true;
            m_callFunction("nms", "CheckKeyboardLayout");
        });

        SetSettingsImpl(settings.vkMode, settings.skMode);
        m_observer = new ns.FocusChangeObserver(OnElementFocus, OnElementBlur, OnSettingsChanged, ["input"]);

        ns.AddEventListener(window, "unload", () =>
        {
            clearTimeout(m_protectChangeTimeout);
            clearTimeout(m_postponeStart);
            m_ready = false;
            m_observer.unbind();
        });
    }

    Init();
}

let instance = null;
ns.RunModule(() =>
{
    if (!instance)
        instance = new VirtualKeyboard();
}, 2000);
});
