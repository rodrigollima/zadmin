class DomainRequest:

    list_domain_request =  """
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
                <GetAllDomainsRequest applyConfig="0" xmlns="urn:zimbraAdmin" />
            </soap:Body>
        </soap:Envelope>
    """

    create_domain_request = """
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
                <CreateDomainRequest name="%s" xmlns="urn:zimbraAdmin"/>
            </soap:Body>
        </soap:Envelope>
    """


    count_accounts_by_class_of_service = """
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
                <CountAccountRequest xmlns="urn:zimbraAdmin">
                    <domain by="name">%s</domain>
                </CountAccountRequest>
            </soap:Body>
        </soap:Envelope>
    """