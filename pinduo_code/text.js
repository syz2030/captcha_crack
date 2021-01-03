function i(e, t, n, r, i, a, u) {
    try {
        var l = e[a](u)
            , c = l.value
    } catch (s) {
        return void n(s)
    }
    l.done ? t(c) : o.a.resolve(c).then(r, i)
}

function a(e) {
    return function () {
        var t = this
            , n = arguments;
        return new o.a(function (r, o) {
                var a = e.apply(t, n);

                function u(e) {
                    i(a, r, o, u, l, "next", e)
                }

                function l(e) {
                    i(a, r, o, u, l, "throw", e)
                }

                u(void 0)
            }
        )
    }
}


y = function () {
    return new i.a(function (t) {
            var e = "";
            if (r) {
                try {
                    e = r.messagePack(d),
                        r.clearCache()
                } catch (n) {
                    console.log("@#@##:", n)
                }
                return t(e)
            }
            return (r ? i.a.resolve(r) : v().then(function (t) {
                return document.body ? (p.serverTime = t,
                    r = new c(p)) : ""
            }, function (t) {
                console.log(t)
            })).then(function (n) {
                return e = n.messagePack(d),
                    n.clearCache(),
                    t(e)
            })
        }
    )
}

y()



