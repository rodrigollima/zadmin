
class AuthRequest:
    
    authenticate = """
        <?xml version="1.0" ?>
        <soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
            <soap:Header>
                <context xmlns="urn:zimbra">
	                <format type="xml"/>
                </context>
            </soap:Header>
            <soap:Body>
                <AuthRequest xmlns="urn:zimbraAdmin">
                    <name>%s</name>
                    <password>%s</password>
                </AuthRequest>
            </soap:Body>
        </soap:Envelope>
    """