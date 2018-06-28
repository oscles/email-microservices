TYPE_ERROR_LIST = ['error', 'warning', 'degub', 'info', ]

ERRORS_LIST = [
    {
        'code': 1020,
        'type': 'error',
        'description': 'LAN Connection Error	LAN communication failure.',
        'body': '''Please check the network settings for your PC and RTR-500W, such as the IP address. (See: Q&A about Settings),
                If the network settings are correct but this error occurs frequently, the FTP/E-mail transmission failure 
                may be repeatedly occurring. 
                Try turning off the transmission of data and warnings via FTP/E-mail and see if that stops the error.'''
    },
    {
        'code': 1022,
        'type': 'warning',
        'description': 'Failure to open USB',
        'body': 'Reinsert the USB cable.'
    },
    {
        'code': 1028,
        'type': 'error',
        'description': 'Reception Timeout Error',
        'body': '''Communication with the device failed. Please wait and try again. 
                If this error occurs frequently, the FTP/E-mail transmission failure may be repeatedly occurring.
                Try turning off the transmission of data and warnings via FTP/E-mail and see if that stops the error.'''
    },
    {
        'code': 20006,
        'type': 'info',
        'description': 'This version of the application is old.',
        'body': 'Update the application to the latest version.'
    },
    {
        'code': 40001,
        'type': 'warning',
        'description': 'La comunicación inalámbrica está ocupada.',
        'body': '''Se está procesando otra sesión de comunicación inalámbrica. 
                Espere y vuelva a intentarlo.'''
    },
    {
        'code': 40002,
        'type': 'error',
        'description': 'Wireless Communication Failure (Remote Unit).',
        'body': '''Cambie las posiciones del dispositivo base, los 
                repetidores o las unidades remotas y vuelva a intentarlo.'''
    },

]
