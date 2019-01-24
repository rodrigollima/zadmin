class AccountRequest:

    create_account_request = """
        <?xml version="1.0" ?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
            <soap:Header>
                <context xmlns="urn:zimbra">
                    <authToken>%s</authToken>
                    <session/>
                    <account by="name">%s</account>
                    <userAgent name="zclient" version="8.0.7_GA_6020"/>
                </context>
            </soap:Header>
            <soap:Body>
                <CreateAccountRequest name="%s" password="%s" xmlns="urn:zimbraAdmin"> 
                    <a n="zimbraCosId">%s</a>
                </CreateAccountRequest>
            </soap:Body>
        </soap:Envelope>
    """