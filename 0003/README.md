## HTTPS 的安全通信机制

> Client：

    * Handshake: ClientHello

> Server:

    * Handshake: ServerHello
    * Handshake: Certificate
    * Handshake: ServerHelloDone
    
> Client:

    * Handshake: ClientKeyExchange
    * ChangeCipherSpec
    * Handshake: Finished

> Server:

    * ChangeCipherSpec
    * Handshake: Finished

> Client:

    * Application Data(HTTP)

> Server:

    * Application Data(HTTP)

> Client:

    * Alert: warning, close notify


FIN close TCP Connections
