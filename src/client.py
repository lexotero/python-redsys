class Client:

    def __init__(self, sandbox: bool = True) -> None:
        """
        Parameters
        ----------
        sandbox: boolean, optional
            If set to True, the client will use the Redsys test environment.
            The default is set to True to prevent accidental request to
            the production environment.
        """
        self.sandbox = sandbox
