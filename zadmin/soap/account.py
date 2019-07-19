class AccountRequest:
    get_all_accounts_request = """
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
                <GetAllAccountsRequest xmlns="urn:zimbraAdmin">
                    <domain by="name">%s</domain>
                </GetAllAccountsRequest>
            </soap:Body>
        </soap:Envelope>
    """

    get_account_request = """
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
                <GetAccountRequest xmlns="urn:zimbraAdmin"> 
                    <account by="name">%s</account>
                </GetAccountRequest>
            </soap:Body>
        </soap:Envelope>
    """

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

    update_account_cos_request = """
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
                <ModifyAccountRequest id="{value-of-zimbra-id}" xmlns="urn:zimbraAdmin">
                    <a n="zimbraCosId">%s</a>
                </ModifyAccountRequest>
            </soap:Body>
        </soap:Envelope>
    """

    update_account_password_request = """
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
                <SetPasswordRequest id="%s" newPassword="%s" xmlns="urn:zimbraAdmin" />
            </soap:Body>
        </soap:Envelope>
    """

    rename_account_request = """
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
                <RenameAccountRequest id="%s" newName="%s" xmlns="urn:zimbraAdmin" /> 
            </soap:Body>
        </soap:Envelope>
    """
