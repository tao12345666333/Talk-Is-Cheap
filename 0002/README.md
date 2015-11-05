## HTTP Headers

* If-Range

**Request**

```
    GET /index.html
    If-Range: "12345"
    Range: bytes=1000-2000
```

**Response**

```
    206 Partial Content
    Content-Range: bytes 1000-2000/5000
    Content-Length: 1000
```

* 只有当实体标记与请求一致的时候，才会返回对应请求部分,否则返回全部.

* 选择If-Range 优于 If-Match 在于如果使用If-Match,但是资源已经更新的情况下,服务器会返回412 Precondition Failed, 催促客户端再次发送请求上来.这样就会增加一次请求了.
