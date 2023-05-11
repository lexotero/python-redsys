from typing import Literal

"""
Parameter types for the REST client.

Official documentation - https://pagosonline.redsys.es/parametros-entrada-salida.html
"""

DS_MERCHANT_AMOUNT = TypeVar


DS_MERCHANT_COF_INI = Literal[
    "S",  # Yes, it is the first COF request
    "N",  # No, it is not the first COF request
    # NOTE: that other values would be "valid", but they are
    # ignored and the transaction is not processed as COF.
    # We prefer to be explicit and if a parameter of this type
    # is used, we make sure the transaction is COF.
]


DS_MERCHANT_COF_TYPE = Literal[
    "I",  # Instalments
    "R",  # Recurring
    "H",  # Reauthorisation
    "E",  # Resubmission
    "D",  # Delayed
    "M",  # Incremental
    "N",  # No show
    "C",  # Other
]


DS_MERCHANT_DIRECTPAYMENT = bool


DS_XPAYORIGEN = Literal["Google", "Apple"]


DS_XPAYTYPE = Literal["WEB", "InApp"]

DS_MERCHANT_SHIPPINGADDRESSPYP = Literal[
    # Whether or not to obtain the registered shipping address of the
    # payee's PayPal account.
    "S",  # Yes
    "N",  # No
]


DS_MERCHANT_EXCEP_SCA = Literal[
    "MIT",
    "LWV",
    "TRA",
    "COR",
    "ATD",
    "NDF",
]


DS_MERCHANT_OTA = Literal[
    "S",
]


class DS_MERCHANT_CONSUMERLANGUAGE(int):
    languages_map = {
        "0": "Spanish (Default)",
        "1": "Spanish",
        "2": "English",
        "3": "Catalan",
        "4": "French",
        "5": "German",
        "6": "Dutch",
        "7": "Italian",
        "9": "Swedish",
        "10": "Valencian",
        "11": "Polish",
        "12": "Galician",
        "13": "Basque",
        "100": "Bulgarian",
        "156": "Chinese",
        "191": "Croatian",
        "203": "Czech",
        "208": "Danish",
        "233": "Estonian",
        "246": "Finish",
        "300": "Greek",
        "348": "Hungarian",
        "392": "Japanese",
        "428": "Latvian",
        "440": "Lithuanian",
        "470": "Maltese",
        "642": "Romanian",
        "643": "Russian",
        "703": "Slovak",
        "705": "Slovenian",
        "792": "Turkish",
    }
    
    def __new__(cls, *value):
        """
        Validate that the value corresponds with the int code of one of the accepted
        languages.
        """
        if (code := str(value[0])):
            if code not in cls.languages_map:
                raise ValueError(
                    f'Bad value "{code}". Valid values are: {cls.languages_map}'
                )
        return int.__new__(cls, *value)


class DS_MERCHANT_CURRENCY(int):
    currencies_map = {
        # NOTE: sorry for the all-caps, copy-paste'd from the official doc.
        "840", "DOLAR U.S.A. USD",
        "826", "POUND STERLING GBP",
        "392", "YEN JPY",
        "32", "ARGENTINE AUSTRAL ARP",
        "36", "AUSTRALIAN DOLLAR AUD",
        "124", "CANADIAN DOLLAR CAD",
        "152", "CHILEAN PESO CLP",
        "170", "COLOMBIAN PESO COP",
        "188", "COSTA RICA COLON CRC",
        "356", "INDIAN RUPEE INR",
        "484", "MEXICAN PESO MXP",
        "604", "PERU INTI PEI",
        "756", "SWISS FRANC CHF",
        "858", "URUGUAYAN PESO UYP",
        "986", "BRAZILIAN REAL BRL",
        "949", "TURKISH LIRA TRY",
        "8", "LEK ALL",
        "12", "ALGERIAN DINAR DZD",
        "24", "ANGOLA KWANZA AOK",
        "30", "PROBANDO DESA MON",
        "31", "AZERBAIJANIAN MANAT AZM",
        "32", "ARGENTINE AUSTRAL ARP",
        "36", "AUSTRALIAN DOLLAR AUD",
        "44", "BAHAMIAN DOLLAR BSD",
        "48", "BAHRAINI DINAR BHD",
        "50", "TAKA BDT"
        "51", "ARMENIAN DRAM AMD",
        "52", "BARBADOS DOLLAR BBD",
        "60", "BERMUDAN DOLLAR BMD",
        "64", "NGULTRUM BTN",
        "68", "BOLIVIAN PESO BOP",
        "70", "DINAR BAD",
        "72", "PULA BWP",
        "76", "CRUZEIRO BRC",
        "84", "BELIZE DOLLAR 084",
        "90", "SOLOMON ISLANDS DOLL SBD",
        "96", "BRUNEI DOLLAR BND",
        "100", "LEV BGL",
        "104", "KYAT BUK",
        "108", "BURUNDI FRANC BIF",
        "112", "BELARUSSIAN RUBLE BYB",
        "116", "RIEL KHR",
        "124", "CANADIAN DOLLAR CAD",
        "132", "CAPE VERDE ESCUDO CVE",
        "136", "CAYMAN ISLANDS DOLLA KYD",
        "144", "SRI LANKA RUPEE LKR",
        "152", "CHILEAN PESO CLP",
        "156", "YUAN RENMINBI CNY",
        "157", "CHINESE RENMIMBI CNH",
        "158", "CHINESE RENMINBI CNX",
        "170", "COLOMBIAN PESO COP",
        "174", "COMOROS FRANC KMF",
        "180", "ZAIRE ZRZ",
        "188", "COSTA RICA COLON CRC",
        "191", "CROATIAN KUNA HRK",
        "192", "CUBAN PESO CUP",
        "196", "CYPRUS POUND CYP",
        "200", "KORUNA CSK",
        "203", "CZECH KORUNA CZK",
        "208", "DANISH KRONE DKK",
        "214", "DOMINICAN PESO DOP",
        "218", "SUCRE ECS",
        "222", "EL SALVADOR COLON SVC",
        "226", "EKWELE GQE",
        "230", "ETHIOPIAN BIRR ETB",
        "232", "ERITREAN NAKTAN ERN",
        "233", "ESTONIAN KROON EEK",
        "238", "FALKLAND ISLANDS FKP",
        "242", "FIJI DOLLAR FJD",
        "262", "DJIBOUTI FRANC DJF",
        "268", "GEORGIAN LARI GEL",
        "270", "DALASI GMD",
        "278", "MARK DER DDR DDM",
        "288", "GHANA CEDI GHC",
        "292", "GIBRALTAR POUND GIP",
        "320", "QUETZAL GTQ",
        "324", "SYLI GNS",
        "328", "GUYANA DOLLAR GYD",
        "332", "GOURDE HTG",
        "340", "LEMPIRA HNL",
        "344", "HONG KONG DOLLAR HKD",
        "348", "FORINT HUF",
        "352", "ICELAND KRONA ISK",
        "356", "INDIAN RUPEE INR",
        "360", "RUPIAH IDR",
        "364", "IRANIAL RIAL IRR",
        "365", "IRANIAN AIRLINE RATE IRA",
        "368", "IRAQI DINAR IQD",
        "376", "ISRAEL SHEKEL ILS",
        "388", "JAMAICAN DOLLAR JMD",
        "392", "YEN JPY",
        "398", "TENGE KZT",
        "400", "JORDANIAN DINAR JOD",
        "404", "KENYAN SHILLING KES",
        "408", "NORTH KOREAN WON KPW",
        "410", "KOREAN WON KRW",
        "414", "KUWAITI DINAR KWD",
        "417", "KYRGYZSTAN SON KGS",
        "418", "KIP LAK",
        "422", "LEBANESE POUND LBP",
        "426", "LESOTHO LOTI LSM",
        "428", "LATVIAN LAT LVL",
        "430", "LIBERIAN DOLLAR LRD",
        "434", "LIBYAN DINAR LYD",
        "440", "LITHUANIAN LITAS LTL",
        "446", "PATACA MOP",
        "450", "MALAGASY FRANC MGF",
        "454", "MALAWI KWACHA MWK",
        "458", "MALASYAN RINGGIT MYR",
        "462", "MALDIVE RUPEE MVR",
        "466", "MALI MLF",
        "470", "MALTESE LIRA MTL",
        "478", "OUGUIYA MRO",
        "480", "MAURITIUS RUPEE MUR",
        "484", "MEXICAN PESO MXP",
        "496", "TUGRIK MNT",
        "498", "MOLDOVIAN LEU MDL",
        "504", "MORROCAN DIRHAM MAD",
        "508", "METICAL MZM",
        "512", "RIAL OMANI OMR",
        "516", "NAMIBIAN DOLLAR NAD",
        "524", "NEPALESE RUPEE NPR",
        "532", "NETHERLANDS ANTILLIA ANG",
        "533", "ARUBA AWG",
        "536", "YUGOSLAVIAN NEW DIAN NTZ",
        "548", "VANUATU VATU VUV",
        "554", "NEW ZEALAND DOLLAR NZD",
        "556", "NAIRA 566",
        "558", "CORDOBA NIC",
        "566", "NAIRA NGN",
        "578", "NORWEGIAN KRONE NOK",
        "582", "PACIFIC ISLAND PCI",
        "586", "PAKISTAN RUPEE PKR",
        "590", "BALBOA PAB",
        "598", "KINA PGK",
        "600", "GUARANI PYG",
        "604", "PERU INTI PEI",
        "608", "PHILIPPINE PESO PHP",
        "616", "ZLOTY PLZ",
        "624", "GUINEA",
        "626", "TIMOR ESCUDO TPE",
        "634", "QATARI RIAL QAR",
        "642", "LEU ROL",
        "643", "RUSSIAN ROUBLE RUB",
        "646", "RWANDA FRANC RWF",
        "654", "ST.HELENA POUND SHP",
        "678", "DOBRA STD",
        "682", "SAUDI RIYAL SAR",
        "690", "SEYCHELLES RUPEE SCR",
        "694", "LEONE SLL",
        "702", "SINGAPORE DOLLAR SGD",
        "703", "SLOVAK KORUNA SKK",
        "704", "DONG VND",
        "705", "SLOVENIAN TOLAR SIT",
        "706", "SOMALI SHILLING SOS",
        "710", "RAND ZAR",
        "716", "ZIMBABWE DOLLAR ZWD",
        "720", "YEMENI DINAR YDD",
        "728", "SOUTH SUDANESE POUND SSP",
        "736", "SUDANESE POUND SDP",
        "737", "SUDAN AIRLINES SDA",
        "740", "SURINAM GUILDER SRG",
        "748", "LILANGENI SZL",
        "752", "SWEDISH KRONA SEK",
        "756", "SWISS FRANC CHF",
        "760", "SYRIAN POUND SYP",
        "762", "TAJIK RUBLE TJR",
        "764", "BAHT THB",
        "776", "PA'ANGA TOP",
        "780", "TRINIDAD Y TOBAGO DO TTD",
        "784", "UAE DIRHAM AED",
        "788", "TUNISIAN DINAR TND",
        "792", "TURKISH LIRA TRL",
        "793", "PSEUDO TURKISH LIRA PTL",
        "795", "MANAT TMM",
        "800", "UGANDA SHILLING UGS",
        "804", "KARBOVANET UAK",
        "807", "MACEDONIAN DENAR MKD",
        "810", "RUSSIAN ROUBLE RUR",
        "818", "EGYPTIAN POUND EGP",
        "826", "POUND STERLING GBP",
        "834", "TANZANIAN SHILLING TZS",
        "840", "DOLAR U.S.A. USD",
        "858", "URUGUAYAN PESO UYP",
        "860", "UZBEKISTAN SUM UZS",
        "862", "BOLIVAR VEB",
        "882", "TALA WST",
        "886", "YEMINI RIAL YER",
        "890", "NEW YUGOSLAVIAN DOLL YUD",
        "891", "NEW DINAR YUG",
        "894", "KWACHA ZMK",
        "901", "NEW TAIWAN DOLLAR TWD",
        "934", "NEW MANAT TMT",
        "936", "GHANA CEDI GHS",
        "941", "DINAR SERBIO RSD",
        "943", "MOZAMBIQUE METICAL MZN",
        "944", "AZERBAIJANIAN MANAT AZN",
        "946", "NEW LEU RON",
        "949", "TURKISH LIRA TRY",
        "950", "CFA FRANC BEAC XAF",
        "951", "EAST CARIBBEAN DOLLA XCD",
        "952", "CFA FRANC BCEAO XOF",
        "953", "CFP FRANC XPF",
        "954", "E.C.U. EUROPEAN CUR XEU",
        "967", "KWACHA ZMW",
        "968", "SURINAME DOLLAR SRD",
        "969", "ARIARY MGA",
        "971", "AFGHANISTAN AFGHANI AFN",
        "972", "TAJIKISTAN SOMONI TJS",
        "973", "KWANZA ANGOLA AOA",
        "974", "BELARUSSIAN RUBLE BYR",
        "975", "NEW LEV BGN",
        "976", "FRANCO DEL CONGO CDF",
        "977", "BOSNIAN MARKA BAM",
        "978", "EURO EUR",
        "980", "HRYVNIA UAH",
        "981", "GEORGIAN LARI GEL",
        "985", "NEW POLISH ZLOTY PLN",
        "986", "BRAZILIAN REAL BRL",
        "991", "RAND FINANCIER ZAL",
    }

    def __new__(cls, *value):
        """
        Validate that the value corresponds with the int code of one of the accepted
        currencies.
        """
        if (code := str(value[0])):
            if code not in cls.currencies_map:
                raise ValueError(
                    f'Bad value "{code}". Valid values are: {cls.currencies_map}'
                )
        return int.__new__(cls, *value)

