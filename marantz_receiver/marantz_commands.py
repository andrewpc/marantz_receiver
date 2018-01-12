"""
Commands and operators used by NAD.

CMDS[domain][function]
"""
CMDS = {
    'main':
        {
            'mute':
                {'cmd': 'AMT',
                 'supported_operators': [':']
                 },
            'power':
                {'cmd': 'PWR',
                 'supported_operators': [':']
                 },
            'volume':
                {'cmd': 'VOL',
                 'supported_operators': [':']
                 },
            'source':
                {'cmd': 'SRC',
                 'supported_operators': [':']
                 },
            'status':
                {'cmd': 'AST',
                 'supported_operators': [':']
                 }
        }
}