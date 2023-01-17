(function(e, u, v) {
    var r = function() {
            var a, c = function() {
                    return null != a ? a : a = function() {
                        var a = [],
                            c = "unknown",
                            b = {
                                trident: 0,
                                gecko: 0,
                                presto: 0,
                                webkit: 0,
                                unknown: -1
                            },
                            d, n = {},
                            c = document.createElement("nadu");
                        for (d in c.style)
                            if (c = (/^([A-Za-z][a-z]*)[A-Z]/.exec(d) || [])[1]) c = c.toLowerCase(), c in n ? n[c]++ : n[c] = 1;
                        for (var g in n) a.push([g, n[g]]);
                        a = a.sort(function(a, c) {
                            return c[1] - a[1]
                        }).slice(0, 10);
                        for (d = 0; d < a.length; d++) switch (a[d][0]) {
                            case "moz":
                                b.gecko += 5;
                                break;
                            case "ms":
                                b.trident += 5;
                                break;
                            case "get":
                                b.webkit++;
                                break;
                            case "webkit":
                                b.webkit += 5;
                                break;
                            case "o":
                                b.presto += 2;
                                break;
                            case "xv":
                                b.presto += 2
                        }
                        "onhelp" in window && b.trident++;
                        "maxConnectionsPerServer" in window && b.trident++;
                        try {
                            void 0 !== window.ActiveXObject.toString && (b.trident += 5)
                        } catch (p) {}
                        void 0 !== function() {}.toSource && (b.gecko += 5);
                        var a = "unknown",
                            e;
                        for (e in b) b[e] > b[a] && (a = e);
                        return a
                    }()
                },
                b = function() {
                    return !!window.opera || !!window.opr && !!window.opr.addons
                },
                d = function() {
                    return !!document.documentMode
                },
                g = function() {
                    return !d() && "undefined" !== typeof CSS &&
                        CSS.supports("(-ms-ime-align:auto)")
                },
                n = function() {
                    return "webkit" == c()
                },
                p = function() {
                    return void 0 !== u.chrome && "Opera Software ASA" != navigator.vendor && void 0 === navigator.msLaunchUri && n()
                };
            return {
                isOpera: b,
                isIE: d,
                isEdge: g,
                isFirefox: function() {
                    return "undefined" !== typeof InstallTrigger
                },
                isWebkit: n,
                isChrome: p,
                isSafari: function() {
                    return !p() && !g() && !b() && "WebkitAppearance" in document.documentElement.style
                }
            }
        }(),
        t = function(a, c, b, d) {
            a.addEventListener ? a.addEventListener(c, b, d) : a.attachEvent && a.attachEvent("on" +
                c, b)
        },
        s = function(a, c, b, d) {
            document.removeEventListener ? a.removeEventListener(c, b, d || !1) : document.detachEvent && a.detachEvent("on" + c, b)
        },
        A = function(a) {
            var c;
            a = a.document;
            "undefined" !== typeof a.hidden ? c = "visibilitychange" : "undefined" !== typeof a.mozHidden ? c = "mozvisibilitychange" : "undefined" !== typeof a.msHidden ? c = "msvisibilitychange" : "undefined" !== typeof a.webkitHidden && (c = "webkitvisibilitychange");
            return c
        },
        F = function(a, c) {
            var b = A(a),
                d = a.document;
            b && t(d, b, c, !1)
        },
        G = function(a) {
            var c = window.addEventListener ?
                "addEventListener" : "attachEvent";
            (0, window[c])("attachEvent" == c ? "onmessage" : "message", function(c) {
                a(c[c.message ? "message" : "data"])
            }, !1)
        },
        H = function(a, c) {
            "function" === typeof a && Math.random() < c / 100 && a.call(this)
        },
        I = function(a, c, b) {
            var d = window.document.createElement("IFRAME");
            d.id = c;
            d.height = "5px";
            d.width = "5px";
            d.src = b ? b : "javascript:'1'";
            d.style.position = "absolute";
            d.style.top = "-10000px";
            d.style.left = "-10000px";
            d.style.visibility = "hidden";
            d.style.opacity = 0;
            window.document.body.appendChild(d);
            try {
                var g =
                    d.contentDocument;
                if (g) {
                    g.open();
                    g.writeln("<!DOCTYPE html><html><head><title></title></head><body></body></html>");
                    g.close();
                    var e = g.createElement("script");
                    e && (e.type = "text/javascript", e.text = a, g.body.appendChild(e))
                }
            } catch (p) {
                n(p, "JS exception while injecting iframe")
            }
            return d
        },
        n = function(a, c) {
            e.ueLogError(a, {
                logLevel: "ERROR",
                attribution: "A9TQForensics",
                message: c
            })
        },
        J = function(a, c, b) {
            a = {
                vfrd: 1 === c ? "8" : "4",
                dbg: a
            };
            "object" === typeof b ? a.info = JSON.stringify(b) : "string" === typeof b && (a.info = b);
            return {
                server: window.location.hostname,
                fmp: a
            }
        };
    (function(a) {
        function c(a, c, b) {
            var d = "chrm msie ffox sfri opra phnt slnm othr extr xpcm invs poev njs cjs rhn clik1 rfs uam clik stln snd nfo hlpx clkh mmh chrm1 chrm2 wgl srvr zdim nomime chrm3 otch ivm.tst ivm.clk mmh2 clkh2 achf nopl slnm1".split(" ");
            y = a < d.length ? d[a] : "othr";
            e.ue && e.ue.event && e.ue.event(J(y, c, b), "a9_tq", "a9_tq.FraudMetrics.3")
        }

        function b() {
            var c = !1,
                f = "",
                b = 6,
                d = function(a, c) {
                    var f, b, k = !1;
                    for (f in a) k = k || -1 < c.indexOf(f);
                    if ("function" === typeof Object.getOwnPropertyNames)
                        for (f =
                            Object.getOwnPropertyNames(a), b = 0; b < f.length; b++) k = k || -1 < c.indexOf(f[b]);
                    if ("function" === typeof Object.keys)
                        for (f = Object.keys(a), b = 0; b < f.length; b++) k = k || -1 < c.indexOf(f[b]);
                    return k
                },
                l = function(a) {
                    try {
                        return !!a.toString().match(/\{\s*\[native code\]\s*\}$/m)
                    } catch (c) {
                        return !1
                    }
                },
                h = 0;
            "undefined" !== typeof _evaluate && -1 < _evaluate.toString().indexOf("browser.runScript") && h++;
            "undefined" !== typeof ArrayBuffer && "undefined" !== typeof print && l(ArrayBuffer) && !l(print) && h++;
            "undefined" !== typeof ABORT_ERR && h++;
            "undefined" !== typeof browser && "undefined" !== typeof browser._windowInScope && "undefined" !== typeof browser._windowInScope._response && h++;
            3 <= h && (c = !0);
            l = [function() {
                if (!0 === d(v, "__webdriver_evaluate __selenium_evaluate __fxdriver_evaluate __driver_evaluate __webdriver_unwrapped __selenium_unwrapped __fxdriver_unwrapped __driver_unwrapped __webdriver_script_function __webdriver_script_func __webdriver_script_fn webdriver _Selenium_IDE_Recorder _selenium calledSelenium $cdc_asdjflasutopfhvcZLmcfl_ $chrome_asyncScriptInfo __$webdriverAsyncExecutor".split(" "))) return !0;
                var c = function(c) {
                        return c.match(/\$[a-z]dc_/) && a.document[c] && a.document[c].cache_
                    },
                    b;
                for (b in v)
                    if (c(b)) return f = b, !0;
                if ("function" === typeof Object.getOwnPropertyNames)
                    for (var k = Object.getOwnPropertyNames(v), m = 0; m < k.length; m++)
                        if (c(k[m])) return f = b, !0;
                return !1
            }, function() {
                return d(a, "_phantom __nightmare _selenium callPhantom callSelenium _Selenium_IDE_Recorder webdriver __webdriverFunc domAutomation domAutomationController __lastWatirAlert __lastWatirConfirm __lastWatirPrompt _WEBDRIVER_ELEM_CACHE".split(" ")) ?
                    !0 : "function" === typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Promise || "function" === typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Array || "function" === typeof a.cdc_adoQpoasnfa76pfcZLmcfl_Symbol ? (b = 39, !0) : !1
            }, function() {
                return a.webdriver || a.document.webdriver || a.document.documentElement.hasAttribute("webdriver") || a.document.documentElement.hasAttribute("selenium") || a.document.documentElement.hasAttribute("driver") || navigator.webdriver || "object" === typeof a.$cdc_asdjflasutopfhvcZLmcfl_ || "object" === typeof a.document.$cdc_asdjflasutopfhvcZLmcfl_ ||
                    null != a.name && -1 < a.name.indexOf("driver") ? (f = null != a.name ? a.name : "", !0) : !1
            }, function() {
                return a.external && "function" === typeof a.external.toString && a.external.toString() && -1 != a.external.toString().indexOf("Sequentum") ? (f = a.external.toString(), !0) : !1
            }];
            for (h = 0; h < l.length; h++)
                if (l[h].call()) {
                    c = !0;
                    break
                } return {
                isSel: c,
                isTest: !1,
                info: f,
                headlessCode: b
            }
        }

        function d() {
            var a = "AddChannel AddDesktopComponent AddFavorite AddSearchProvider AddService AddToFavoritesBar AutoCompleteSaveForm AutoScan bubbleEvent ContentDiscoveryReset ImportExportFavorites InPrivateFilteringEnabled IsSearchProviderInstalled IsServiceInstalled IsSubscribed msActiveXFilteringEnabled msAddSiteMode msAddTrackingProtectionList msClearTile msEnableTileNotificationQueue msEnableTileNotificationQueueForSquare150x150 msEnableTileNotificationQueueForSquare310x310 msEnableTileNotificationQueueForWide310x150 msIsSiteMode msIsSiteModeFirstRun msPinnedSiteState msProvisionNetworks msRemoveScheduledTileNotification msReportSafeUrl msScheduledTileNotification msSiteModeActivate msSiteModeAddButtonStyle msSiteModeAddJumpListItem msSiteModeAddThumbBarButton msSiteModeClearBadge msSiteModeClearIconOverlay msSiteModeClearJumpList msSiteModeCreateJumpList msSiteModeRefreshBadge msSiteModeSetIconOverlay msSiteModeShowButtonStyle msSiteModeShowJumpList msSiteModeShowThumbBar msSiteModeUpdateThumbBarButton msStartPeriodicBadgeUpdate msStartPeriodicTileUpdate msStartPeriodicTileUpdateBatch msStopPeriodicBadgeUpdate msStopPeriodicTileUpdate msTrackingProtectionEnabled NavigateAndFind raiseEvent setContextMenu ShowBrowserUI menuArguments onvisibilitychange scrollbar selectableContent version visibility mssitepinned AddUrlAuthentication CloseRegPopup FeatureEnabled GetJsonWebData GetRegValue Log LogShellErrorsOnly OpenPopup ReadFile RunGutsScript SaveRegInfo SetAppMaximizeTimeToRestart SetAppMinimizeTimeToRestart SetAutoStart SetAutoStartMinimized SetMaxMemory ShareEventFromBrowser ShowPopup ShowRadar WriteFile WriteRegValue summonWalrus".split(" "),
                f = -1,
                b, d;
            "Microsoft Internet Explorer" === navigator.appName ? (b = navigator.userAgent, d = /MSIE ([0-9]{1,}[\.0-9]{0,})/, null !== d.exec(b) && (f = parseFloat(RegExp.$1))) : "Netscape" === navigator.appName && (b = navigator.userAgent, d = /Trident\/.*rv:([0-9]{1,}[\.0-9]{0,})/, null !== d.exec(b) && (f = parseFloat(RegExp.$1)));
            if (-1 === f && null === navigator.userAgent.match(/Windows Phone/) && window.external) {
                for (b = f = 0; b < a.length; b++)
                    if ("unknown" === typeof window.external[a[b]]) {
                        f++;
                        break
                    } 0 < f && c(17)
            }
        }

        function g() {
            var a = Math.random().toString(36).substr(2),
                b = null;
            G(function(d) {
                try {
                    var q = d.split(" ");
                    if (null !== b && q[0] === a && 0 < q[1].length) {
                        var l = JSON.parse(q[1]);
                        for (d = 0; d < l.length; d++) 1 == d && "R29vZ2xlIFN3aWZ0U2hhZGVy" == l[d] && c(27)
                    }
                } catch (h) {}
            });
            b = I('(function fg45s() {                     var payload = [];                     var canvas = document.createElement("canvas");                     var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl") || canvas.getContext("moz-webgl");                     if (gl != null) {                         var debugInfo = gl.getExtension("WEBGL_debug_renderer_info");                         if (debugInfo != null) {                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL)));                             payload.push(btoa(gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL)));                             parent.postMessage(window.frameElement.id + " " + JSON.stringify(payload), parent.location.origin);                         }                     }                 }             )();',
                a);
            window.setTimeout(function() {
                try {
                    b && document.body && b.parentNode === document.body && document.body.removeChild(b), b = null
                } catch (a) {
                    n(a, "JS exception while removing iframe")
                }
            }, 5E3)
        }

        function u() {
            function b() {
                s(a, "mousemove", d);
                s(a, "click", f)
            }

            function f() {
                try {
                    c(23), b(), s(a.document, h, q)
                } catch (f) {
                    n(f, "JS exception - detectClickDuringTabInactive")
                }
            }

            function d() {
                try {
                    l || (l = !0, c(24), b(), s(a.document, h, q))
                } catch (f) {
                    n(f, "JS exception - detectMouseMovementsDuringTabInactive")
                }
            }

            function q() {
                try {
                    var c;
                    "undefined" !==
                    typeof document.hidden ? c = "hidden" : "undefined" !== typeof document.mozHidden ? c = "mozHidden" : "undefined" !== typeof document.msHidden ? c = "msHidden" : "undefined" !== typeof document.webkitHidden && (c = "webkitHidden");
                    !0 !== document[c] === !1 ? (t(a, "mousemove", d, !1), t(a, "click", f, !1)) : b()
                } catch (h) {
                    n(h, "JS exception - handleVisibilityChangeDuringTabInactive")
                }
            }
            var l = !1,
                h = A(a);
            F(a, q)
        }
        var p = function() {
                var a = window.navigator,
                    c = a.vendor,
                    b = "undefined" !== typeof window.opr,
                    d = -1 < a.userAgent.indexOf("Edg"),
                    a = /Chrome/.test(a.userAgent);
                return /Google Inc\./.test(c) && a && !b && !d
            }(),
            y = null,
            B = function(a) {
                var b = [],
                    d = (new Date).getTime(),
                    q = function() {
                        s(a, "mousemove", l);
                        s(a, "click", h)
                    },
                    l = function(a) {
                        try {
                            var k = (new Date).getTime();
                            if (!(100 > k - d)) {
                                b.push({
                                    x: a.clientX,
                                    y: a.clientY
                                });
                                if (50 < b.length && (b.shift(), !(50 > b.length))) {
                                    var h = b[0].x,
                                        m = b[49].x,
                                        l = b[0].y,
                                        e = b[49].y;
                                    a = e - l;
                                    for (var g = h - m, h = l * m - h * e, m = a / g * -1, p = b[49].ts - b[0].ts, l = !0, e = 0; e < b.length; e++)
                                        if (0 != a * b[e].x + g * b[e].y + h) {
                                            l = !1;
                                            break
                                        }! 0 == l && (p = {
                                        grdt: m,
                                        tmsp: p
                                    }, q(), c(19, 0, p))
                                }
                                d = k
                            }
                        } catch (r) {
                            n(r,
                                "JS exception - recordHoverPosition")
                        }
                    },
                    h = function(a) {
                        try {
                            var d = a.clientX,
                                h = a.clientY,
                                k = {
                                    hcc: b.length,
                                    cx: d,
                                    cy: h
                                };
                            if (0 === b.length) q(), c(18, 0, k);
                            else if (null != d && null != h) {
                                var l;
                                k.hpos = b;
                                var e = b[b.length - 1];
                                l = Math.sqrt(Math.pow(d - e.x, 2) + Math.pow(h - e.y, 2));
                                100 < l && (k.hcc = b.length, k.cx = d, k.cy = h, k.dhp = l, q(), c(15, 0, k))
                            }
                        } catch (g) {
                            n(g, "JS exception - checkClick")
                        }
                    };
                t(a, "mousemove", l, !1);
                t(a, "click", h, !1)
            },
            C = function() {
                if (r.isFirefox()) {
                    var a = 0;
                    void 0 !== window.onstorage && a++;
                    var b = document.createElement("div");
                    b.style.wordSpacing = "22%";
                    "22%" === b.style.wordSpacing && a++;
                    "function" === typeof b.getAttributeNames && a++;
                    b = document.createElement("script");
                    b.type = "text/javascript";
                    b.text = "class Rectangle {             constructor(height, width) {                 this.height = height;                 this.width = width;             }             get area() {                 return this.calcArea();             }             calcArea() {                 return this.height * this.width;             }             }             const square = new Rectangle(10, 10);             window.__random__str = square.area;";
                    document.body.appendChild(b);
                    100 === window.__random__str && a++;
                    b && document.body && document.body.removeChild(b);
                    2 < a && (void 0 === window.onabsolutedeviceorientation || void 0 === navigator.permissions) && c(37, 0, a)
                }
            },
            w = function() {
                return null === navigator.userAgent.match(/(iPad|iPhone|iPod|android|webOS)/i)
            },
            D = function() {
                var a = function(a, b) {
                        for (var c, d = "", f = {}, k = {}, e = 0, m = 0; m < b.length; m++) k[b[m]] = String.fromCharCode(126 - m);
                        var e = 0,
                            g;
                        for (g in a) - 1 < b.indexOf(g) && (f[g] = 1, e++);
                        d = d + e + "!";
                        if ("function" === typeof Object.getOwnPropertyNames) {
                            c =
                                Object.getOwnPropertyNames(a);
                            for (m = e = 0; m < c.length; m++) - 1 < b.indexOf(c[m]) && (f[c[m]] = 1, e++);
                            d = d + e + "!"
                        }
                        if ("function" === typeof Object.keys) {
                            c = Object.keys(a);
                            for (m = e = 0; m < c.length; m++) - 1 < b.indexOf(c[m]) && (f[c[m]] = 1, e++);
                            d = d + e + "!"
                        }
                        if ("prototype" in Object && "hasOwnProperty" in Object.prototype)
                            for (g in f) Object.prototype.hasOwnProperty.call(f, g) && (d += k[g]);
                        else
                            for (g in f) d += k[g];
                        return encodeURIComponent(d)
                    },
                    b = document.createElement("nadu"),
                    a = {
                        w: a(window, "SVGFESpotLightElement XMLHttpRequestEventTarget onratechange StereoPannerNode dolphinInfo VTTCue globalStorage WebKitCSSRegionRule MozSmsFilter MediaController mozInnerScreenX onwebkitwillrevealleft DOMMatrix GeckoActiveXObject MediaQueryListEvent PhoneNumberService ServiceWorkerContainer yandex vc2hxtaq9c NavigatorDeviceStorage HTMLHtmlElement ScreenOrientation MSGesture mozCancelRequestAnimationFrame GetSVGDocument MediaSource webkitMediaStream DeviceMotionEvent webkitPostMessage doNotTrack WebKitMediaKeyError HTMLCollection InstallTrigger StorageObsolete CustomEvent orientation XMLHttpRequest Worker showModelessDialog EventSource onmouseleave SVGAnimatedPathData TouchList TextTrackCue onanimationend HTMLBodyElement fluid MSFrameUITab Generator SecurityPolicyViolationEvent ClientRectList SmartCardEvent CSSSupportsRule mmbrowser".split(" ")),
                        c: a(b.style, "XvPhonemes MozTextAlignLast webkitFilter MozPerspective msTextSizeAdjust OAnimationFillMode borderImageSource MozOSXFontSmoothing border-inline-start-color MozOsxFontSmoothing columns touchAction scroll-snap-coordinate webkitAnimationFillMode webkitLineSnap webkitGridAutoColumns animationDuration isolation overflowWrap offsetRotation webkitShapeOutside MozOpacity position justifySelf borderRight webkitMatchNearestMailBlockquoteColor msImeAlign parentRule MozColumnFill cssText borderRightStyle textOverflow webkitGridRow webkitBackgroundComposite length -moz-column-fill enableBackground flex-basis".split(" "))
                    };
                e.ue && e.ue.event && (a = {
                    vfrd: "0",
                    info: JSON.stringify(a)
                }, e.ue.event({
                    server: window.location.hostname,
                    fmp: a
                }, "a9_tq", "a9_tq.FraudMetrics.3"))
            };
        try {
            (a.callPhantom || a._phantom || a.PhantomEmitter || a.__phantomas || /PhantomJS/.test(navigator.userAgent)) && c(5);
            a.Buffer && c(12);
            a.emit && c(13);
            a.spawn && c(14);
            (null != a.domAutomation || null != a.domAutomationController || null != a._WEBDRIVER_ELEM_CACHE || /HeadlessChrome/.test(navigator.userAgent) || "" === navigator.languages) && c(0);
            if (r.isChrome() && a.webkitRequestFileSystem) a.webkitRequestFileSystem(a.TEMPORARY,
                1,
                function() {},
                function() {
                    c(0)
                });
            else if (r.isSafari() && a.localStorage) {
                try {
                    a.localStorage.setItem("__nadu", "")
                } catch (K) {
                    c(3)
                }
                a.localStorage.removeItem("__nadu")
            }!w() || navigator.mimeTypes && 0 != navigator.mimeTypes.length || (p ? c(30, 0, "chrm") : r.isFirefox() && c(30, 0, "ff"));
            r.isWebkit() && p && w() && (void 0 === a.chrome && c(0), a.chrome && a.chrome.app && !1 !== a.chrome.app.isInstalled && void 0 !== navigator.languages && c(31));
            a.external && "function" === typeof a.external.toString && a.external.toString() && -1 < a.external.toString().indexOf("RuntimeObject") &&
                c(8);
            a.FirefoxInterfaces && "function" === typeof a.FirefoxInterfaces && a.FirefoxInterfaces("wdICoordinate", "wdIMouse", "wdIStatus") && c(2);
            a.XPCOMUtils && c(9);
            (a.Components && (a.Components.interfaces && a.Components.interfaces.nsICommandProcessor || a.Components.wdICoordinate || a.Components.wdIMouse || a.Components.wdIStatus || a.Components.classes) || a.netscape && a.netscape.security && a.netscape.security.privilegemanager) && c(8);
            a.isExternalUrlSafeForNavigation && c(1);
            !a.opera || null === a.opera._browserjsran || 0 !== a.opera._browserjsran &&
                !1 !== a.opera._browserjsran || c(4);
            a.screen && (1 >= a.screen.availHeight || 1 >= a.screen.availWidth || 1 >= a.screen.height || 1 >= a.screen.width || 0 >= a.screen.devicePixelRatio) && c(10);
            var x = window.setInterval(function() {
                try {
                    var a = b();
                    a.isSel && (c(a.headlessCode, !0 === a.isTest ? 1 : 0, a.info), window.clearInterval(x))
                } catch (d) {
                    window.clearInterval(x), n(d, "JS exception - detectSelenium")
                }
            }, 1E3);
            window.setTimeout(function() {
                window.clearInterval(x)
            }, 1E4);
            var z = a.PointerEvent;
            a.PointerEvent = function() {
                c(11);
                if (void 0 !== z) {
                    var a =
                        Array.prototype.slice.call(arguments);
                    return new z(a)
                }
                return null
            };
            d();
            B(a);
            u();
            g();
            0 !== a.outerHeight && 0 !== a.outerWidth || c(29);
            C();
            !w() || navigator.plugins && 0 != navigator.plugins.length || (p ? c(38, 0, "chrm") : r.isFirefox() && c(38, 0, "ff"));
            H(D, 10);
            !a.chrome || a.chrome.csi || a.chrome.loadTimes || c(25)
        } catch (E) {
            n(E, "JS exception - ")
        }
    })(u)
})(ue_csm, window, document);
