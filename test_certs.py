#!/usr/bin/python3

from six import b

# httpbin Root CA cert
root_ca_cert_pem = b("""-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
""")

# httpbin Int CA cert
int_ca_cert_pem = b("""-----BEGIN CERTIFICATE-----
MIIESTCCAzGgAwIBAgITBntQXCplJ7wevi2i0ZmY7bibLDANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MTAyMTIyMjQzNFoXDTQwMTAyMTIyMjQzNFowRjEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEVMBMGA1UECxMMU2VydmVyIENB
IDFCMQ8wDQYDVQQDEwZBbWF6b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQDCThZn3c68asg3Wuw6MLAd5tES6BIoSMzoKcG5blPVo+sDORrMd4f2AbnZ
cMzPa43j4wNxhplty6aUKk4T1qe9BOwKFjwK6zmxxLVYo7bHViXsPlJ6qOMpFge5
blDP+18x+B26A0piiQOuPkfyDyeR4xQghfj66Yo19V+emU3nazfvpFA+ROz6WoVm
B5x+F2pV8xeKNR7u6azDdU5YVX1TawprmxRC1+WsAYmz6qP+z8ArDITC2FMVy2fw
0IjKOtEXc/VfmtTFch5+AfGYMGMqqvJ6LcXiAhqG5TI+Dr0RtM88k+8XUBCeQ8IG
KuANaL7TiItKZYxK1MMuTJtV9IblAgMBAAGjggE7MIIBNzASBgNVHRMBAf8ECDAG
AQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUWaRmBlKge5WSPKOUByeW
dFv5PdAwHwYDVR0jBBgwFoAUhBjMhTTsvAyUlC4IWZzHshBOCggwewYIKwYBBQUH
AQEEbzBtMC8GCCsGAQUFBzABhiNodHRwOi8vb2NzcC5yb290Y2ExLmFtYXpvbnRy
dXN0LmNvbTA6BggrBgEFBQcwAoYuaHR0cDovL2NybC5yb290Y2ExLmFtYXpvbnRy
dXN0LmNvbS9yb290Y2ExLmNlcjA/BgNVHR8EODA2MDSgMqAwhi5odHRwOi8vY3Js
LnJvb3RjYTEuYW1hem9udHJ1c3QuY29tL3Jvb3RjYTEuY3JsMBMGA1UdIAQMMAow
CAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IBAQAfsaEKwn17DjAbi/Die0etn+PE
gfY/I6s8NLWkxGAOUfW2o+vVowNARRVjaIGdrhAfeWHkZI6q2pI0x/IJYmymmcWa
ZaW/2R7DvQDtxCkFkVaxUeHvENm6IyqVhf6Q5oN12kDSrJozzx7I7tHjhBK7V5Xo
TyS4NU4EhSyzGgj2x6axDd1hHRjblEpJ80LoiXlmUDzputBXyO5mkcrplcVvlIJi
WmKjrDn2zzKxDX5nwvkskpIjYlJcrQu4iCX1/YwZ1yNqF9LryjlilphHCACiHbhI
RnGfN8j8KLDVmWyTYMk8V+6j0LI4+4zFh2upqGMQHL3VFVFWBek6vCDWhB/b
-----END CERTIFICATE-----
""")

# httpbin Leaf cert
good_leaf_cert_pem = b("""-----BEGIN CERTIFICATE-----
MIIFbjCCBFagAwIBAgIQC6tW9S/J9yHIw1v8WOnMPDANBgkqhkiG9w0BAQsFADBG
MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRUwEwYDVQQLEwxTZXJ2ZXIg
Q0EgMUIxDzANBgNVBAMTBkFtYXpvbjAeFw0yMDAxMTgwMDAwMDBaFw0yMTAyMTgx
MjAwMDBaMBYxFDASBgNVBAMTC2h0dHBiaW4ub3JnMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEApFxnGvqYGUel320/nRE281GA6WAOVwY+Npl79AIz45bH
XcxNu+LeMEuGBvrl2EuccQJGXpCY8+sCzFRmcCZsMtTzUdj6R/QbWR7OFjf6Z6w1
AiKccc7iKlRUF/tWAuoLr1b6L9+JfAkJAUL35VV7/vIs9IZ8uWJDhEB2wU6rRZO+
2RBvHGM7oeBNda1/maukjLNYmJ+pxSnrsRTMh3dHUCxZ47h2UZhj2SWCPlW+SMsY
NM/JkURnzSy0lgq/woVeM5g4nOpWuljO1scJ0ZRbR3I+3JveGEd3sQi8e6HkWFtI
mGklhirXxE/t86GP86s+XbwnABIML12h09M3mTJqEwIDAQABo4IChjCCAoIwHwYD
VR0jBBgwFoAUWaRmBlKge5WSPKOUByeWdFv5PdAwHQYDVR0OBBYEFE1H1xvaOuX7
0DFAys411lS5yO+lMCUGA1UdEQQeMByCC2h0dHBiaW4ub3Jngg0qLmh0dHBiaW4u
b3JnMA4GA1UdDwEB/wQEAwIFoDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUH
AwIwOwYDVR0fBDQwMjAwoC6gLIYqaHR0cDovL2NybC5zY2ExYi5hbWF6b250cnVz
dC5jb20vc2NhMWIuY3JsMCAGA1UdIAQZMBcwCwYJYIZIAYb9bAECMAgGBmeBDAEC
ATB1BggrBgEFBQcBAQRpMGcwLQYIKwYBBQUHMAGGIWh0dHA6Ly9vY3NwLnNjYTFi
LmFtYXpvbnRydXN0LmNvbTA2BggrBgEFBQcwAoYqaHR0cDovL2NydC5zY2ExYi5h
bWF6b250cnVzdC5jb20vc2NhMWIuY3J0MAwGA1UdEwEB/wQCMAAwggEEBgorBgEE
AdZ5AgQCBIH1BIHyAPAAdgDuS723dc5guuFCaR+r4Z5mow9+X7By2IMAxHuJeqj9
ywAAAW+2QhJbAAAEAwBHMEUCIQCBAIJ4tACBrdHwB4ZnGIGTy3/9FxuZ9GIoHgfX
5RjefQIgeXY+x7oWQmIShXCrBSdqeTYXrsxQcWE6ZpAyQxcsdUUAdgCHdb/nWXz4
jEOZX73zbv9WjUdWNv9KtWDBtOr/XqCDDwAAAW+2QhKqAAAEAwBHMEUCIBDMYim2
sF8eHpW1Z7/yQ1liTwa8IRSjidBd9ZVIwe6mAiEA7DPOTaRgc/cH3OzIGSu6dLae
e5F/YRkmC9TikWiWTC8wDQYJKoZIhvcNAQELBQADggEBAIIERQYarXyjBoi2yjhr
7WTjbsPLTUSUFVK2f+qckuDJfoX9bW1PLShve5R8WWgIBu4eZYyUDS+BzXXSV2wg
NscAL9TkxobI/N0HiI5iGtJuI8dVIsFSRMG9IWRz96/pqRcTMz5GlIhAurB3aR+S
MnwAYsrNBHG+rqgUwNVn0h2XoVJe3VxrV2QwTH5kzBwG/Ju1+Khqkvs+9/M3UrJg
qPGwissH0W8HgYWhKVISkN2ui55RgbHXQHYDX0uYgGK6iRMxHHlOR1vOqRgEvVGF
5g8CcK3EzritKaHkD6bf0pnSE/E7cjKXzgB4l+58dsNcIVo9YgID4xYGS6paetso
XHE=
-----END CERTIFICATE-----
""")

# localhost Leaf cert
bad_leaf_cert_pem = b("""-----BEGIN CERTIFICATE-----
MIIDHjCCAgagAwIBAgIBBTANBgkqhkiG9w0BAQsFADBEMR0wGwYDVQQDDBRydXN0
eU1hZ25ldEludENBMjAyMzELMAkGA1UEBhMCR0IxFjAUBgkqhkiG9w0BCQEWB3JA
ci5jb20wHhcNMjAwMzE4MTI1MzQ5WhcNMjEwMzE4MTI1MzQ5WjA9MRYwFAYDVQQD
DA05MDA2MTEzLmxvY2FsMQswCQYDVQQGEwJHQjEWMBQGCSqGSIb3DQEJARYHckBy
LmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKlqQm3+T5tO3acs
ZC5ll7DciJ5DkvaV37DDDwQXgUkKZVgeRPmuooRBdmri8Soiislt1LKO3a2lOoh2
KugEKJoDVdnXqHV38iI2Gh5usRnMEecmKMrD5dy8cDjOHg4UIPaq1N0F9IGvMUMR
5AUADFrjps+K3cOg9nmRPmmDO/W+4rWcwL5RgjB61xF550LsV/JsXXy2Ztz9cYCK
l0A9J9i+E2ESBPj78mYL5aiiKWoyKUeCDDDArvVyHUm41caNXqDKI3EJ7WD1kQg/
ReR1vzQw6NH+8+8MQnqk5wQeAtsfRX34jViWv4+557dK2bPuCbpVG7O0HNGKr+Ud
0AtmxhUCAwEAAaMiMCAwHgYDVR0RBBcwFYINOTAwNjExMy5sb2NhbIcEwKgAJTAN
BgkqhkiG9w0BAQsFAAOCAQEAcVKIRXRmPTdtyQFFEFs6Ujb7p1HtOeGM9+kDocGs
8rJp7EUcSW7n2O/zz9eg4FJ/X3L77GXMSNi6jDeHbRSPm6PQQmgxR9sWNur5WTMZ
2lvtaFbbH8ftoJzFWkpox0W18Ifh+bXn/KsjA7rI5dJ7GapuYVQU47d+NcTKGkSd
QaVVLcq68u4H0IQy0/Zx9fc2H247VchY/mZrh8nmAHzoov0k3b4CGh7F3aludU+V
TQLjKz2eVLE2jNga0JdW+qYa2jaGfbTfM5MIh7Um+ovT2BFdjEF74ced/XdGISAb
eZQ29ZRpZWE1ydq9YLCmq1GT5wa3D97AxU5c/XSSvQGMaw==
-----END CERTIFICATE-----
""")