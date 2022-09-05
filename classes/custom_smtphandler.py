from logging import Handler, getLogger

log = getLogger(__name__)


class HTMLSMTPHandler(Handler):
    """
    A handler class which sends an SMTP email for each logging event.
    """

    def __init__(
        self,
        mailhost,
        fromaddr,
        toaddrs,
        subject,
        credentials=None,
        secure=None,
        timeout=5.0,
        message_type=None,
    ):
        """
        Initialize the handler.
        Initialize the instance with the from and to addresses and subject
        line of the email. To specify a non-standard SMTP port, use the
        (host, port) tuple format for the mailhost argument. To specify
        authentication credentials, supply a (username, password) tuple
        for the credentials argument. To specify the use of a secure
        protocol (TLS), pass in a tuple for the secure argument. This will
        only be used when authentication credentials are supplied. The tuple
        will be either an empty tuple, or a single-value tuple with the name
        of a keyfile, or a 2-value tuple with the names of the keyfile and
        certificate file. (This tuple is passed to the `starttls` method).
        A timeout in seconds can be specified for the SMTP connection (the
        default is one second).
        """
        Handler.__init__(self)
        if isinstance(mailhost, (list, tuple)):
            self.mailhost, self.mailport = mailhost
        else:
            self.mailhost, self.mailport = mailhost, None
        if isinstance(credentials, (list, tuple)):
            self.username, self.password = credentials
        else:
            self.username = None
        self.fromaddr = fromaddr
        if isinstance(toaddrs, str):
            toaddrs = [toaddrs]
        self.toaddrs = toaddrs
        self.subject = subject
        self.secure = secure
        self.timeout = timeout
        self.type = message_type

    def getSubject(self, record):
        """
        Determine the subject for the email.
        If you want to specify a subject line which is record-dependent,
        override this method.
        """
        subject = f"[{record.levelno}] {record.levelname} - {self.subject}"
        return subject

    def emit(self, record):
        # print(
        #     f"""The record is {record}. Some attributes of record are {record.__dict__}\n
        #     Record Message: {record.msg}
        #     Record Name: {record.name}
        #     Record Level Name: {record.levelname}
        #     Record Level No: {record.levelno}
        #     Record Args: {record.args}
        #     Record Created: {record.created}
        #     Record Exc Info: {record.exc_info}
        #     Record Exc Text: {record.exc_text}
        #     Record Filename: {record.filename}
        #     Record Func Name: {record.funcName}
        #     Record Line No: {record.lineno}
        #     Record Module: {record.module}R
        #     ecord Msecs: {record.msecs}
        #     Record Process: {record.process}
        #     Record Process Name: {record.processName}
        #     Record Relative Created: {record.relativeCreated}
        #     Record Stack Info: {record.stack_info}
        #     Record Thread: {record.thread}
        #     Record Thread Name: {record.threadName}
        #     Record Args: {record.args}
        #     Record Asctime: {record.asctime}
        #     Record Message Long: {record.message}
        #     Record Pathname: {record.pathname}
        #     """
        # )
        """
        Emit a record.
        Format the record and send it to the specified addressees.
        """
        try:
            import email.utils
            import smtplib
            from email.message import EmailMessage

            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port, timeout=self.timeout)
            msg = EmailMessage()
            msg["From"] = self.fromaddr
            msg["To"] = ",".join(self.toaddrs)
            msg["Subject"] = self.getSubject(record)
            msg["Date"] = email.utils.localtime()
            if self.type == "PLAIN":
                msg.set_content(self.format(record))
            elif self.type == "HTML":
                html_msg = email.utils.make_msgid()
                msg.add_alternative(
                    f"{self.format(record)}",
                    subtype="html",
                    cid=html_msg[1:-1],
                )
            elif self.type == "HYBRID":
                html_msg = email.utils.make_msgid()
                plaintext, html = record.msg.split("||")

                msg.add_alternative(
                    f"""\{self.format(html)}""", subtype="html", cid=html_msg[1:-1]
                )
                msg.set_content(self.format(plaintext))

            if self.username:
                if self.secure is not None:
                    smtp.ehlo()
                    smtp.starttls(*self.secure)
                    smtp.ehlo()
                smtp.login(self.username, self.password)
            smtp.send_message(msg)
            smtp.quit()
        except Exception:
            self.handleError(record)
