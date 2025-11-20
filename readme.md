# 2025 年改版后的江西省高考报名系统

管理员网址 https://jxgk.jxeea.cn/admin/login

## 1.新建虚拟环境

```bash
python3 -m venv ./.venv
```

## 2.激活虚拟环境

```bash
source ./.venv/bin/activate
或者
.venv\Scripts\activate.bat
```

## account.py 文件内容

```python
account={
    'username':'xxxxxx',
    'password':'yyyyyy'
}
```

## 用 python3 生成这样格式的字符串 2025-11-20 10:29:49s

```python
from datetime import datetime

# 获取当前时间并格式化为指定格式
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(current_time)
```

## 密码加密算法分析

```js
添加xhr断点`sso/ssoLogin.rest`;
// https://jxgk.jxeea.cn/ksy/js/AdminLogin.LKPQem9P.js

{
  if (x.username.length <= 0 || x.password.length <= 0) return (f.error = "请输入账号、密码！"), !1;
  if ("1" == f.smsEnable && x.code.length <= 0) return (f.error = "请输入验证码！"), !1;
  (e.username = x.username),
    (e.password = o.doEncrypt(x.password + "_" + a.$dayjs().format("YYYY-MM-DD HH:mm:ss"))),
    (e.code = x.code),
    (e.captchaId = x.captchaId);
}

// https://jxgk.jxeea.cn/ksy/js/index.hcNrbTQ4.js

e = "#ydzxgk2026#_2025-11-20 10:29:49";
let oe = {
  doEncrypt: function (e) {
    return o.sm2.doEncrypt(
      e.trim(),
      "04d5982dcb21ad8bd5df69bc63984c2ae6550fcb2aae5cb1941afc76146a0570ea532fe1695e6103b888b2af4f7ad15b1c07a33a8ba8ad02205dc24b20ebb287f7",
      1
    );
  },
};

// sm2加密算法
// https://jxgk.jxeea.cn/ksy/js/vendor.A_2TN0mi.js
// t="#ydzxgk2026#_2025-11-20 10:29:49"
// e="04d5982dcb21ad8bd5df69bc63984c2ae6550fcb2aae5cb1941afc76146a0570ea532fe1695e6103b888b2af4f7ad15b1c07a33a8ba8ad02205dc24b20ebb287f7"
doEncrypt:function(t, e, r=1) {
        t = "string" == typeof t ? Wl.hexToArray(Wl.utf8ToHex(t)) : Array.prototype.slice.call(t),
        e = Wl.getGlobalCurve().decodePointHex(e);
        const n = Wl.generateKeyPairHex()
          , o = new Hl(n.privateKey,16);
        let i = n.publicKey;
        i.length > 128 && (i = i.substr(i.length - 128));
        const s = e.multiply(o)
          , a = Wl.hexToArray(Wl.leftPad(s.getX().toBigInteger().toRadix(16), 64))
          , l = Wl.hexToArray(Wl.leftPad(s.getY().toBigInteger().toRadix(16), 64))
          , c = Wl.arrayToHex(Vl([].concat(a, t, l)));
        let u = 1
          , f = 0
          , p = [];
        const h = [].concat(a, l)
          , d = () => {
            p = Vl([...h, u >> 24 & 255, u >> 16 & 255, u >> 8 & 255, 255 & u]),
            u++,
            f = 0
        }
        ;
        d();
        for (let m = 0, y = t.length; m < y; m++)
            f === p.length && d(),
            t[m] ^= 255 & p[f++];
        const g = Wl.arrayToHex(t);
        return 0 === r ? i + g + c : i + c + g
    }
```
