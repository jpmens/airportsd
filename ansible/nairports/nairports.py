#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random


airports = [
 {
  "cc": "SB",
  "lat": "-9.428",
  "lon": "160.054993",
  "iata": "HIR",
  "name": "Honiara International Airport"
 },
 {
  "cc": "PG",
  "lat": "-9.443380355834961",
  "lon": "147.22000122070312",
  "iata": "POM",
  "name": "Port Moresby Jacksons International Airport"
 },
 {
  "cc": "BB",
  "lat": "0.03",
  "lon": "-0.07",
  "iata": "",
  "name": "Delete spam"
 },
 {
  "cc": "IS",
  "lat": "63.985001",
  "lon": "-22.6056",
  "iata": "KEF",
  "name": "Keflavik International Airport"
 },
 {
  "cc": "CA",
  "lat": "53.3097",
  "lon": "-113.580002",
  "iata": "YEG",
  "name": "Edmonton International Airport"
 },
 {
  "cc": "CA",
  "lat": "44.8807983398",
  "lon": "-63.5085983276",
  "iata": "YHZ",
  "name": "Halifax / Stanfield International Airport"
 },
 {
  "cc": "CA",
  "lat": "45.322498",
  "lon": "-75.669197",
  "iata": "YOW",
  "name": "Ottawa Macdonald-Cartier International Airport"
 },
 {
  "cc": "CA",
  "lat": "46.7911",
  "lon": "-71.393303",
  "iata": "YQB",
  "name": "Quebec Jean Lesage International Airport"
 },
 {
  "cc": "CA",
  "lat": "45.467837",
  "lon": "-73.742294",
  "iata": "YUL",
  "name": "Montreal / Pierre Elliott Trudeau International Airport"
 },
 {
  "cc": "CA",
  "lat": "49.193901062",
  "lon": "-123.183998108",
  "iata": "YVR",
  "name": "Vancouver International Airport"
 },
 {
  "cc": "CA",
  "lat": "49.909999847399995",
  "lon": "-97.2398986816",
  "iata": "YWG",
  "name": "Winnipeg / James Armstrong Richardson International Airport"
 },
 {
  "cc": "CA",
  "lat": "51.118822",
  "lon": "-114.009933",
  "iata": "YYC",
  "name": "Calgary International Airport"
 },
 {
  "cc": "CA",
  "lat": "47.618599",
  "lon": "-52.7519",
  "iata": "YYT",
  "name": "St. John's International Airport"
 },
 {
  "cc": "CA",
  "lat": "43.6772",
  "lon": "-79.6306",
  "iata": "YYZ",
  "name": "Toronto Lester B. Pearson International Airport"
 },
 {
  "cc": "DZ",
  "lat": "36.693886",
  "lon": "3.214531",
  "iata": "ALG",
  "name": "Houari Boumediene Airport"
 },
 {
  "cc": "GH",
  "lat": "5.605189800262451",
  "lon": "-0.16678600013256073",
  "iata": "ACC",
  "name": "Kotoka International Airport"
 },
 {
  "cc": "NG",
  "lat": "9.00679",
  "lon": "7.26317",
  "iata": "ABV",
  "name": "Nnamdi Azikiwe International Airport"
 },
 {
  "cc": "NG",
  "lat": "6.5773701667785645",
  "lon": "3.321160078048706",
  "iata": "LOS",
  "name": "Murtala Muhammed International Airport"
 },
 {
  "cc": "NE",
  "lat": "13.4815",
  "lon": "2.18361",
  "iata": "NIM",
  "name": "Diori Hamani International Airport"
 },
 {
  "cc": "TN",
  "lat": "36.851002",
  "lon": "10.2272",
  "iata": "TUN",
  "name": "Tunis Carthage International Airport"
 },
 {
  "cc": "BE",
  "lat": "50.901402",
  "lon": "4.48444",
  "iata": "BRU",
  "name": "Brussels Airport"
 },
 {
  "cc": "DE",
  "lat": "52.362247",
  "lon": "13.500672",
  "iata": "BER",
  "name": "Berlin Brandenburg Airport"
 },
 {
  "cc": "DE",
  "lat": "50.030241",
  "lon": "8.561096",
  "iata": "FRA",
  "name": "Frankfurt Airport"
 },
 {
  "cc": "DE",
  "lat": "53.630402",
  "lon": "9.98823",
  "iata": "HAM",
  "name": "Hamburg Helmut Schmidt Airport"
 },
 {
  "cc": "DE",
  "lat": "50.865898",
  "lon": "7.14274",
  "iata": "CGN",
  "name": "Cologne Bonn Airport"
 },
 {
  "cc": "DE",
  "lat": "51.289501",
  "lon": "6.76678",
  "iata": "DUS",
  "name": "D\u00fcsseldorf Airport"
 },
 {
  "cc": "DE",
  "lat": "48.353802",
  "lon": "11.7861",
  "iata": "MUC",
  "name": "Munich Airport"
 },
 {
  "cc": "DE",
  "lat": "49.498699",
  "lon": "11.078056",
  "iata": "NUE",
  "name": "Nuremberg Airport"
 },
 {
  "cc": "DE",
  "lat": "51.420657",
  "lon": "12.232705",
  "iata": "LEJ",
  "name": "Leipzig/Halle Airport"
 },
 {
  "cc": "DE",
  "lat": "48.689899",
  "lon": "9.22196",
  "iata": "STR",
  "name": "Stuttgart Airport"
 },
 {
  "cc": "DE",
  "lat": "52.461102",
  "lon": "9.68508",
  "iata": "HAJ",
  "name": "Hannover Airport"
 },
 {
  "cc": "EE",
  "lat": "59.41443",
  "lon": "24.832706",
  "iata": "TLL",
  "name": "Lennart Meri Tallinn Airport"
 },
 {
  "cc": "FI",
  "lat": "60.318363",
  "lon": "24.963341",
  "iata": "HEL",
  "name": "Helsinki Vantaa Airport"
 },
 {
  "cc": "GB",
  "lat": "54.6575012207",
  "lon": "-6.2158298492399995",
  "iata": "BFS",
  "name": "Belfast International Airport"
 },
 {
  "cc": "GB",
  "lat": "52.453899",
  "lon": "-1.74803",
  "iata": "BHX",
  "name": "Birmingham International Airport"
 },
 {
  "cc": "GB",
  "lat": "53.349375",
  "lon": "-2.279521",
  "iata": "MAN",
  "name": "Manchester Airport"
 },
 {
  "cc": "GB",
  "lat": "51.874699",
  "lon": "-0.368333",
  "iata": "LTN",
  "name": "London Luton Airport"
 },
 {
  "cc": "GB",
  "lat": "51.148771",
  "lon": "-0.192089",
  "iata": "LGW",
  "name": "London Gatwick Airport"
 },
 {
  "cc": "GB",
  "lat": "51.4706",
  "lon": "-0.461941",
  "iata": "LHR",
  "name": "London Heathrow Airport"
 },
 {
  "cc": "GB",
  "lat": "55.871899",
  "lon": "-4.43306",
  "iata": "GLA",
  "name": "Glasgow International Airport"
 },
 {
  "cc": "GB",
  "lat": "55.950145",
  "lon": "-3.372288",
  "iata": "EDI",
  "name": "Edinburgh Airport"
 },
 {
  "cc": "GB",
  "lat": "51.884998",
  "lon": "0.235",
  "iata": "STN",
  "name": "London Stansted Airport"
 },
 {
  "cc": "NL",
  "lat": "52.308601",
  "lon": "4.76389",
  "iata": "AMS",
  "name": "Amsterdam Airport Schiphol"
 },
 {
  "cc": "NL",
  "lat": "51.4500999451",
  "lon": "5.37452983856",
  "iata": "EIN",
  "name": "Eindhoven Airport"
 },
 {
  "cc": "CN",
  "lat": "30.341178",
  "lon": "115.03926",
  "iata": "EHU",
  "name": "Ezhou Huahu Airport"
 },
 {
  "cc": "IE",
  "lat": "53.428713",
  "lon": "-6.262121",
  "iata": "DUB",
  "name": "Dublin Airport"
 },
 {
  "cc": "IE",
  "lat": "52.702",
  "lon": "-8.92482",
  "iata": "SNN",
  "name": "Shannon Airport"
 },
 {
  "cc": "DK",
  "lat": "55.740496",
  "lon": "9.160452",
  "iata": "BLL",
  "name": "Billund Airport"
 },
 {
  "cc": "DK",
  "lat": "55.617900848389",
  "lon": "12.656000137329",
  "iata": "CPH",
  "name": "Copenhagen Kastrup Airport"
 },
 {
  "cc": "LU",
  "lat": "49.6233333",
  "lon": "6.2044444",
  "iata": "LUX",
  "name": "Luxembourg-Findel International Airport"
 },
 {
  "cc": "NO",
  "lat": "60.2934",
  "lon": "5.21814",
  "iata": "BGO",
  "name": "Bergen Airport, Flesland"
 },
 {
  "cc": "NO",
  "lat": "60.193901",
  "lon": "11.1004",
  "iata": "OSL",
  "name": "Oslo Airport, Gardermoen"
 },
 {
  "cc": "NO",
  "lat": "69.683296",
  "lon": "18.9189",
  "iata": "TOS",
  "name": "Troms\u00f8 Airport, Langnes"
 },
 {
  "cc": "NO",
  "lat": "63.457802",
  "lon": "10.924",
  "iata": "TRD",
  "name": "Trondheim Airport, V\u00e6rnes"
 },
 {
  "cc": "NO",
  "lat": "58.876701",
  "lon": "5.63778",
  "iata": "SVG",
  "name": "Stavanger Airport, Sola"
 },
 {
  "cc": "PL",
  "lat": "54.377602",
  "lon": "18.4662",
  "iata": "GDN",
  "name": "Gda\u0144sk Lech Wa\u0142\u0119sa Airport"
 },
 {
  "cc": "PL",
  "lat": "50.077702",
  "lon": "19.7848",
  "iata": "KRK",
  "name": "Krak\u00f3w John Paul II International Airport"
 },
 {
  "cc": "PL",
  "lat": "52.1656990051",
  "lon": "20.967100143399996",
  "iata": "WAW",
  "name": "Warsaw Chopin Airport"
 },
 {
  "cc": "SE",
  "lat": "57.662799835205",
  "lon": "12.279800415039",
  "iata": "GOT",
  "name": "Gothenburg-Landvetter Airport"
 },
 {
  "cc": "SE",
  "lat": "59.64849",
  "lon": "17.928829",
  "iata": "ARN",
  "name": "Stockholm-Arlanda Airport"
 },
 {
  "cc": "LV",
  "lat": "56.923599",
  "lon": "23.9711",
  "iata": "RIX",
  "name": "Riga International Airport"
 },
 {
  "cc": "LT",
  "lat": "54.634102",
  "lon": "25.285801",
  "iata": "VNO",
  "name": "Vilnius International Airport"
 },
 {
  "cc": "ZA",
  "lat": "-33.9648017883",
  "lon": "18.6016998291",
  "iata": "CPT",
  "name": "Cape Town International Airport"
 },
 {
  "cc": "ZA",
  "lat": "-29.6144444444",
  "lon": "31.1197222222",
  "iata": "DUR",
  "name": "King Shaka International Airport"
 },
 {
  "cc": "ZA",
  "lat": "-26.1392",
  "lon": "28.246",
  "iata": "JNB",
  "name": "OR Tambo International Airport"
 },
 {
  "cc": "BW",
  "lat": "-24.555201",
  "lon": "25.9182",
  "iata": "GBE",
  "name": "Sir Seretse Khama International Airport"
 },
 {
  "cc": "SZ",
  "lat": "-26.358611",
  "lon": "31.716944",
  "iata": "SHO",
  "name": "King Mswati III International Airport"
 },
 {
  "cc": "MU",
  "lat": "-20.430201",
  "lon": "57.683601",
  "iata": "MRU",
  "name": "Sir Seewoosagur Ramgoolam International Airport"
 },
 {
  "cc": "ZM",
  "lat": "-15.330833",
  "lon": "28.452722",
  "iata": "LUN",
  "name": "Kenneth Kaunda International Airport"
 },
 {
  "cc": "RE",
  "lat": "-20.890087",
  "lon": "55.518894",
  "iata": "RUN",
  "name": "Roland Garros Airport"
 },
 {
  "cc": "MG",
  "lat": "-18.7969",
  "lon": "47.478802",
  "iata": "TNR",
  "name": "Ivato Airport"
 },
 {
  "cc": "AO",
  "lat": "-8.85837",
  "lon": "13.2312",
  "iata": "LAD",
  "name": "Quatro de Fevereiro International Airport"
 },
 {
  "cc": "MZ",
  "lat": "-25.920799",
  "lon": "32.572601",
  "iata": "MPM",
  "name": "Maputo Airport"
 },
 {
  "cc": "SC",
  "lat": "-4.67434",
  "lon": "55.521801",
  "iata": "SEZ",
  "name": "Seychelles International Airport"
 },
 {
  "cc": "TD",
  "lat": "12.1337",
  "lon": "15.034",
  "iata": "NDJ",
  "name": "N'Djamena International Airport"
 },
 {
  "cc": "ZW",
  "lat": "-17.931801",
  "lon": "31.0928",
  "iata": "HRE",
  "name": "Robert Gabriel Mugabe International Airport"
 },
 {
  "cc": "NA",
  "lat": "-22.4799",
  "lon": "17.4709",
  "iata": "WDH",
  "name": "Hosea Kutako International Airport"
 },
 {
  "cc": "CD",
  "lat": "-4.38575",
  "lon": "15.4446",
  "iata": "FIH",
  "name": "Ndjili International Airport"
 },
 {
  "cc": "ML",
  "lat": "12.5335",
  "lon": "-7.94994",
  "iata": "BKO",
  "name": "Modibo Keita International Airport"
 },
 {
  "cc": "GM",
  "lat": "13.338",
  "lon": "-16.652201",
  "iata": "BJL",
  "name": "Banjul International Airport"
 },
 {
  "cc": "ES",
  "lat": "28.4527",
  "lon": "-13.8638",
  "iata": "FUE",
  "name": "Fuerteventura Airport"
 },
 {
  "cc": "ES",
  "lat": "27.9319",
  "lon": "-15.3866",
  "iata": "LPA",
  "name": "Gran Canaria Airport"
 },
 {
  "cc": "ES",
  "lat": "28.945499",
  "lon": "-13.6052",
  "iata": "ACE",
  "name": "C\u00e9sar Manrique-Lanzarote Airport"
 },
 {
  "cc": "ES",
  "lat": "28.0445",
  "lon": "-16.5725",
  "iata": "TFS",
  "name": "Tenerife Sur Airport"
 },
 {
  "cc": "SL",
  "lat": "8.61644",
  "lon": "-13.1955",
  "iata": "FNA",
  "name": "Lungi International Airport"
 },
 {
  "cc": "LR",
  "lat": "6.23379",
  "lon": "-10.3623",
  "iata": "ROB",
  "name": "Roberts International Airport"
 },
 {
  "cc": "MA",
  "lat": "33.3675",
  "lon": "-7.58997",
  "iata": "CMN",
  "name": "Mohammed V International Airport"
 },
 {
  "cc": "SN",
  "lat": "14.67",
  "lon": "-17.073333",
  "iata": "DSS",
  "name": "Blaise Diagne International Airport"
 },
 {
  "cc": "MR",
  "lat": "18.31",
  "lon": "-15.969722",
  "iata": "NKC",
  "name": "Nouakchott\u2013Oumtounsy International Airport"
 },
 {
  "cc": "CV",
  "lat": "16.7414",
  "lon": "-22.9494",
  "iata": "SID",
  "name": "Am\u00edlcar Cabral International Airport"
 },
 {
  "cc": "VN",
  "lat": "0.0196",
  "lon": "0.0178",
  "iata": "XHG",
  "name": "(Spam)C\u00e1c C\u1ed5ng Game Casino Tr\u1ef1c Tuy\u1ebfn Uy T\u00edn Nh\u1ea5t 2024"
 },
 {
  "cc": "ET",
  "lat": "8.97789",
  "lon": "38.799301",
  "iata": "ADD",
  "name": "Addis Ababa Bole International Airport"
 },
 {
  "cc": "DJ",
  "lat": "11.5473",
  "lon": "43.1595",
  "iata": "JIB",
  "name": "Djibouti-Ambouli Airport"
 },
 {
  "cc": "EG",
  "lat": "30.111534",
  "lon": "31.396694",
  "iata": "CAI",
  "name": "Cairo International Airport"
 },
 {
  "cc": "EG",
  "lat": "27.176776",
  "lon": "33.796692",
  "iata": "HRG",
  "name": "Hurghada International Airport"
 },
 {
  "cc": "EG",
  "lat": "27.977272",
  "lon": "34.394717",
  "iata": "SSH",
  "name": "Sharm El Sheikh International Airport"
 },
 {
  "cc": "SS",
  "lat": "4.87201",
  "lon": "31.601101",
  "iata": "JUB",
  "name": "Juba International Airport"
 },
 {
  "cc": "KE",
  "lat": "-1.31923997402",
  "lon": "36.9277992249",
  "iata": "NBO",
  "name": "Jomo Kenyatta International Airport"
 },
 {
  "cc": "KE",
  "lat": "-4.03483",
  "lon": "39.5942",
  "iata": "MBA",
  "name": "Moi International Airport"
 },
 {
  "cc": "LY",
  "lat": "32.89177",
  "lon": "13.287878",
  "iata": "MJI",
  "name": "Mitiga International Airport"
 },
 {
  "cc": "RW",
  "lat": "-1.96863",
  "lon": "30.1395",
  "iata": "KGL",
  "name": "Kigali International Airport"
 },
 {
  "cc": "SD",
  "lat": "15.5895",
  "lon": "32.5532",
  "iata": "KRT",
  "name": "Khartoum International Airport"
 },
 {
  "cc": "TZ",
  "lat": "-6.87811",
  "lon": "39.202599",
  "iata": "DAR",
  "name": "Julius Nyerere International Airport"
 },
 {
  "cc": "TZ",
  "lat": "-6.22202",
  "lon": "39.224899",
  "iata": "ZNZ",
  "name": "Abeid Amani Karume International Airport"
 },
 {
  "cc": "UG",
  "lat": "0.042386",
  "lon": "32.443501",
  "iata": "EBB",
  "name": "Entebbe International Airport"
 },
 {
  "cc": "ID",
  "lat": "-7.750278",
  "lon": "111.947222",
  "iata": "DHX",
  "name": "Dhoho International Airport"
 },
 {
  "cc": "IN",
  "lat": "15.744257",
  "lon": "73.860625",
  "iata": "GOX",
  "name": "Manohar International Airport"
 },
 {
  "cc": "US",
  "lat": "35.039976",
  "lon": "-106.608925",
  "iata": "ABQ",
  "name": "Albuquerque International Sunport"
 },
 {
  "cc": "US",
  "lat": "38.810799",
  "lon": "-76.866997",
  "iata": "ADW",
  "name": "Joint Base Andrews"
 },
 {
  "cc": "US",
  "lat": "33.6367",
  "lon": "-84.428101",
  "iata": "ATL",
  "name": "Hartsfield Jackson Atlanta International Airport"
 },
 {
  "cc": "US",
  "lat": "30.197535",
  "lon": "-97.662015",
  "iata": "AUS",
  "name": "Austin Bergstrom International Airport"
 },
 {
  "cc": "US",
  "lat": "41.93851",
  "lon": "-72.688066",
  "iata": "BDL",
  "name": "Bradley International Airport"
 },
 {
  "cc": "US",
  "lat": "36.1245",
  "lon": "-86.6782",
  "iata": "BNA",
  "name": "Nashville International Airport"
 },
 {
  "cc": "US",
  "lat": "42.36197",
  "lon": "-71.0079",
  "iata": "BOS",
  "name": "Logan International Airport"
 },
 {
  "cc": "US",
  "lat": "42.940498",
  "lon": "-78.732201",
  "iata": "BUF",
  "name": "Buffalo Niagara International Airport"
 },
 {
  "cc": "US",
  "lat": "39.1754",
  "lon": "-76.668297",
  "iata": "BWI",
  "name": "Baltimore/Washington International Thurgood Marshall Airport"
 },
 {
  "cc": "US",
  "lat": "41.411701",
  "lon": "-81.8498",
  "iata": "CLE",
  "name": "Cleveland Hopkins International Airport"
 },
 {
  "cc": "US",
  "lat": "35.2140007019043",
  "lon": "-80.94309997558594",
  "iata": "CLT",
  "name": "Charlotte Douglas International Airport"
 },
 {
  "cc": "US",
  "lat": "34.213699",
  "lon": "-119.094002",
  "iata": "",
  "name": "Camarillo International Airport"
 },
 {
  "cc": "US",
  "lat": "39.998001",
  "lon": "-82.891899",
  "iata": "CMH",
  "name": "John Glenn Columbus International Airport"
 },
 {
  "cc": "US",
  "lat": "39.048801",
  "lon": "-84.667801",
  "iata": "CVG",
  "name": "Cincinnati Northern Kentucky International Airport"
 },
 {
  "cc": "US",
  "lat": "38.8521",
  "lon": "-77.037697",
  "iata": "DCA",
  "name": "Ronald Reagan Washington National Airport"
 },
 {
  "cc": "US",
  "lat": "39.861698150635",
  "lon": "-104.672996521",
  "iata": "DEN",
  "name": "Denver International Airport"
 },
 {
  "cc": "US",
  "lat": "32.896801",
  "lon": "-97.038002",
  "iata": "DFW",
  "name": "Dallas Fort Worth International Airport"
 },
 {
  "cc": "US",
  "lat": "42.21377",
  "lon": "-83.353786",
  "iata": "DTW",
  "name": "Detroit Metropolitan Wayne County Airport"
 },
 {
  "cc": "US",
  "lat": "40.692501",
  "lon": "-74.168701",
  "iata": "EWR",
  "name": "Newark Liberty International Airport"
 },
 {
  "cc": "US",
  "lat": "26.072599",
  "lon": "-80.152702",
  "iata": "FLL",
  "name": "Fort Lauderdale Hollywood International Airport"
 },
 {
  "cc": "US",
  "lat": "38.9445",
  "lon": "-77.455803",
  "iata": "IAD",
  "name": "Washington Dulles International Airport"
 },
 {
  "cc": "US",
  "lat": "29.984399795532227",
  "lon": "-95.34140014648438",
  "iata": "IAH",
  "name": "George Bush Intercontinental Houston Airport"
 },
 {
  "cc": "US",
  "lat": "39.7173",
  "lon": "-86.294403",
  "iata": "IND",
  "name": "Indianapolis International Airport"
 },
 {
  "cc": "US",
  "lat": "30.492469",
  "lon": "-81.687813",
  "iata": "JAX",
  "name": "Jacksonville International Airport"
 },
 {
  "cc": "US",
  "lat": "40.639447",
  "lon": "-73.779317",
  "iata": "JFK",
  "name": "John F Kennedy International Airport"
 },
 {
  "cc": "US",
  "lat": "36.083361",
  "lon": "-115.151817",
  "iata": "LAS",
  "name": "Harry Reid International Airport"
 },
 {
  "cc": "US",
  "lat": "33.942501",
  "lon": "-118.407997",
  "iata": "LAX",
  "name": "Los Angeles International Airport"
 },
 {
  "cc": "US",
  "lat": "40.777199",
  "lon": "-73.872597",
  "iata": "LGA",
  "name": "La Guardia Airport"
 },
 {
  "cc": "US",
  "lat": "39.2976",
  "lon": "-94.713898",
  "iata": "MCI",
  "name": "Kansas City International Airport"
 },
 {
  "cc": "US",
  "lat": "28.429399490356445",
  "lon": "-81.30899810791016",
  "iata": "MCO",
  "name": "Orlando International Airport"
 },
 {
  "cc": "US",
  "lat": "41.785999",
  "lon": "-87.752403",
  "iata": "MDW",
  "name": "Chicago Midway International Airport"
 },
 {
  "cc": "US",
  "lat": "35.0424",
  "lon": "-89.9767",
  "iata": "MEM",
  "name": "Memphis International Airport"
 },
 {
  "cc": "US",
  "lat": "25.79319953918457",
  "lon": "-80.29060363769531",
  "iata": "MIA",
  "name": "Miami International Airport"
 },
 {
  "cc": "US",
  "lat": "42.947201",
  "lon": "-87.896599",
  "iata": "MKE",
  "name": "General Mitchell International Airport"
 },
 {
  "cc": "US",
  "lat": "44.880081",
  "lon": "-93.221741",
  "iata": "MSP",
  "name": "Minneapolis\u2013Saint Paul International Airport / Wold\u2013Chamberlain Field"
 },
 {
  "cc": "US",
  "lat": "29.993401",
  "lon": "-90.258003",
  "iata": "MSY",
  "name": "Louis Armstrong New Orleans International Airport"
 },
 {
  "cc": "US",
  "lat": "37.720085",
  "lon": "-122.221184",
  "iata": "OAK",
  "name": "Metropolitan Oakland International Airport"
 },
 {
  "cc": "US",
  "lat": "35.393388",
  "lon": "-97.598248",
  "iata": "OKC",
  "name": "Will Rogers World Airport"
 },
 {
  "cc": "US",
  "lat": "41.3032",
  "lon": "-95.894096",
  "iata": "OMA",
  "name": "Eppley Airfield"
 },
 {
  "cc": "US",
  "lat": "34.056",
  "lon": "-117.600998",
  "iata": "ONT",
  "name": "Ontario International Airport"
 },
 {
  "cc": "US",
  "lat": "41.9786",
  "lon": "-87.9048",
  "iata": "ORD",
  "name": "Chicago O'Hare International Airport"
 },
 {
  "cc": "US",
  "lat": "36.895341",
  "lon": "-76.201",
  "iata": "ORF",
  "name": "Norfolk International Airport"
 },
 {
  "cc": "US",
  "lat": "26.683201",
  "lon": "-80.095596",
  "iata": "PBI",
  "name": "Palm Beach International Airport"
 },
 {
  "cc": "US",
  "lat": "45.588699",
  "lon": "-122.598",
  "iata": "PDX",
  "name": "Portland International Airport"
 },
 {
  "cc": "US",
  "lat": "39.871899",
  "lon": "-75.241096",
  "iata": "PHL",
  "name": "Philadelphia International Airport"
 },
 {
  "cc": "US",
  "lat": "33.435302",
  "lon": "-112.005905",
  "iata": "PHX",
  "name": "Phoenix Sky Harbor International Airport"
 },
 {
  "cc": "US",
  "lat": "40.491501",
  "lon": "-80.232903",
  "iata": "PIT",
  "name": "Pittsburgh International Airport"
 },
 {
  "cc": "US",
  "lat": "41.725038",
  "lon": "-71.425668",
  "iata": "PVD",
  "name": "Theodore Francis Green State Airport"
 },
 {
  "cc": "US",
  "lat": "43.646198",
  "lon": "-70.309303",
  "iata": "PWM",
  "name": "Portland International Jetport"
 },
 {
  "cc": "US",
  "lat": "35.877602",
  "lon": "-78.787498",
  "iata": "RDU",
  "name": "Raleigh Durham International Airport"
 },
 {
  "cc": "US",
  "lat": "37.505199",
  "lon": "-77.319702",
  "iata": "RIC",
  "name": "Richmond International Airport"
 },
 {
  "cc": "US",
  "lat": "39.4991",
  "lon": "-119.767998",
  "iata": "RNO",
  "name": "Reno Tahoe International Airport"
 },
 {
  "cc": "US",
  "lat": "26.53619956970215",
  "lon": "-81.75520324707031",
  "iata": "RSW",
  "name": "Southwest Florida International Airport"
 },
 {
  "cc": "US",
  "lat": "32.7336006165",
  "lon": "-117.190002441",
  "iata": "SAN",
  "name": "San Diego International Airport"
 },
 {
  "cc": "US",
  "lat": "29.533701",
  "lon": "-98.469803",
  "iata": "SAT",
  "name": "San Antonio International Airport"
 },
 {
  "cc": "US",
  "lat": "32.127602",
  "lon": "-81.202103",
  "iata": "SAV",
  "name": "Savannah Hilton Head International Airport"
 },
 {
  "cc": "US",
  "lat": "38.1744",
  "lon": "-85.736",
  "iata": "SDF",
  "name": "Louisville Muhammad Ali International Airport"
 },
 {
  "cc": "US",
  "lat": "47.447943",
  "lon": "-122.310276",
  "iata": "SEA",
  "name": "Seattle\u2013Tacoma International Airport"
 },
 {
  "cc": "US",
  "lat": "28.777599334716797",
  "lon": "-81.23750305175781",
  "iata": "SFB",
  "name": "Orlando Sanford International Airport"
 },
 {
  "cc": "US",
  "lat": "37.619806",
  "lon": "-122.374821",
  "iata": "SFO",
  "name": "San Francisco International Airport"
 },
 {
  "cc": "US",
  "lat": "37.362452",
  "lon": "-121.929188",
  "iata": "SJC",
  "name": "Norman Y. Mineta San Jose International Airport"
 },
 {
  "cc": "US",
  "lat": "40.78886",
  "lon": "-111.979866",
  "iata": "SLC",
  "name": "Salt Lake City International Airport"
 },
 {
  "cc": "US",
  "lat": "38.6954",
  "lon": "-121.591003",
  "iata": "SMF",
  "name": "Sacramento International Airport"
 },
 {
  "cc": "US",
  "lat": "33.675701",
  "lon": "-117.867996",
  "iata": "SNA",
  "name": "John Wayne Orange County International Airport"
 },
 {
  "cc": "US",
  "lat": "27.394631",
  "lon": "-82.554359",
  "iata": "SRQ",
  "name": "Sarasota Bradenton International Airport"
 },
 {
  "cc": "US",
  "lat": "38.748697",
  "lon": "-90.370003",
  "iata": "STL",
  "name": "St Louis Lambert International Airport"
 },
 {
  "cc": "US",
  "lat": "43.11119842529297",
  "lon": "-76.1063003540039",
  "iata": "SYR",
  "name": "Syracuse Hancock International Airport"
 },
 {
  "cc": "US",
  "lat": "27.9755",
  "lon": "-82.533203",
  "iata": "TPA",
  "name": "Tampa International Airport"
 },
 {
  "cc": "US",
  "lat": "36.19839859008789",
  "lon": "-95.88809967041016",
  "iata": "TUL",
  "name": "Tulsa International Airport"
 },
 {
  "cc": "AL",
  "lat": "41.4147",
  "lon": "19.7206",
  "iata": "TIA",
  "name": "Tirana International Airport Mother Teresa"
 },
 {
  "cc": "BG",
  "lat": "42.56959915161133",
  "lon": "27.515199661254883",
  "iata": "BOJ",
  "name": "Burgas Airport"
 },
 {
  "cc": "BG",
  "lat": "42.696357",
  "lon": "23.417671",
  "iata": "SOF",
  "name": "Sofia Airport"
 },
 {
  "cc": "BG",
  "lat": "43.232101",
  "lon": "27.8251",
  "iata": "VAR",
  "name": "Varna Airport"
 },
 {
  "cc": "CY",
  "lat": "34.875099",
  "lon": "33.624901",
  "iata": "LCA",
  "name": "Larnaca International Airport"
 },
 {
  "cc": "HR",
  "lat": "45.742901",
  "lon": "16.0688",
  "iata": "ZAG",
  "name": "Zagreb Airport"
 },
 {
  "cc": "ES",
  "lat": "38.2822",
  "lon": "-0.558156",
  "iata": "ALC",
  "name": "Alicante-Elche Miguel Hern\u00e1ndez Airport"
 },
 {
  "cc": "ES",
  "lat": "41.2971",
  "lon": "2.07846",
  "iata": "BCN",
  "name": "Josep Tarradellas Barcelona-El Prat Airport"
 },
 {
  "cc": "ES",
  "lat": "38.872898",
  "lon": "1.37312",
  "iata": "IBZ",
  "name": "Ibiza Airport"
 },
 {
  "cc": "ES",
  "lat": "40.471926",
  "lon": "-3.56264",
  "iata": "MAD",
  "name": "Adolfo Su\u00e1rez Madrid\u2013Barajas Airport"
 },
 {
  "cc": "ES",
  "lat": "36.6749",
  "lon": "-4.49911",
  "iata": "AGP",
  "name": "M\u00e1laga-Costa del Sol Airport"
 },
 {
  "cc": "ES",
  "lat": "39.551701",
  "lon": "2.73881",
  "iata": "PMI",
  "name": "Palma de Mallorca Airport"
 },
 {
  "cc": "ES",
  "lat": "42.896301",
  "lon": "-8.41514",
  "iata": "SCQ",
  "name": "Santiago-Rosal\u00eda de Castro Airport"
 },
 {
  "cc": "FR",
  "lat": "44.8283",
  "lon": "-0.715556",
  "iata": "BOD",
  "name": "Bordeaux-M\u00e9rignac Airport"
 },
 {
  "cc": "FR",
  "lat": "43.629101",
  "lon": "1.36382",
  "iata": "TLS",
  "name": "Toulouse-Blagnac Airport"
 },
 {
  "cc": "FR",
  "lat": "45.725556",
  "lon": "5.081111",
  "iata": "LYS",
  "name": "Lyon Saint-Exup\u00e9ry Airport"
 },
 {
  "cc": "FR",
  "lat": "43.438088",
  "lon": "5.2125",
  "iata": "MRS",
  "name": "Marseille Provence Airport"
 },
 {
  "cc": "FR",
  "lat": "43.658401",
  "lon": "7.21587",
  "iata": "NCE",
  "name": "Nice-C\u00f4te d'Azur Airport"
 },
 {
  "cc": "FR",
  "lat": "49.012798",
  "lon": "2.55",
  "iata": "CDG",
  "name": "Charles de Gaulle International Airport"
 },
 {
  "cc": "FR",
  "lat": "48.72333",
  "lon": "2.37944",
  "iata": "ORY",
  "name": "Paris-Orly Airport"
 },
 {
  "cc": "FR",
  "lat": "47.60068",
  "lon": "7.521117",
  "iata": "BSL",
  "name": "EuroAirport Basel-Mulhouse-Freiburg"
 },
 {
  "cc": "GR",
  "lat": "37.936401",
  "lon": "23.9445",
  "iata": "ATH",
  "name": "Athens Eleftherios Venizelos International Airport"
 },
 {
  "cc": "GR",
  "lat": "35.339699",
  "lon": "25.1803",
  "iata": "HER",
  "name": "Heraklion International Nikos Kazantzakis Airport"
 },
 {
  "cc": "GR",
  "lat": "40.51928",
  "lon": "22.970009",
  "iata": "SKG",
  "name": "Thessaloniki Macedonia International Airport"
 },
 {
  "cc": "HU",
  "lat": "47.43018",
  "lon": "19.262393",
  "iata": "BUD",
  "name": "Budapest Liszt Ferenc International Airport"
 },
 {
  "cc": "IT",
  "lat": "41.138901",
  "lon": "16.760599",
  "iata": "BRI",
  "name": "Bari Karol Wojty\u0142a Airport"
 },
 {
  "cc": "IT",
  "lat": "40.6576",
  "lon": "17.947001",
  "iata": "BDS",
  "name": "Brindisi Airport"
 },
 {
  "cc": "IT",
  "lat": "37.466801",
  "lon": "15.0664",
  "iata": "CTA",
  "name": "Catania-Fontanarossa Airport"
 },
 {
  "cc": "IT",
  "lat": "38.175999",
  "lon": "13.091",
  "iata": "PMO",
  "name": "Falcone\u2013Borsellino Airport"
 },
 {
  "cc": "IT",
  "lat": "39.251499",
  "lon": "9.05428",
  "iata": "CAG",
  "name": "Cagliari Elmas Airport"
 },
 {
  "cc": "IT",
  "lat": "45.6306",
  "lon": "8.72811",
  "iata": "MXP",
  "name": "Milan Malpensa International Airport"
 },
 {
  "cc": "IT",
  "lat": "45.670725",
  "lon": "9.709223",
  "iata": "BGY",
  "name": "Milan Bergamo Airport / Antonio Locatelli Air Base"
 },
 {
  "cc": "IT",
  "lat": "45.200802",
  "lon": "7.64963",
  "iata": "TRN",
  "name": "Turin Airport"
 },
 {
  "cc": "IT",
  "lat": "44.5354",
  "lon": "11.2887",
  "iata": "BLQ",
  "name": "Bologna Guglielmo Marconi Airport"
 },
 {
  "cc": "IT",
  "lat": "45.394955",
  "lon": "10.887303",
  "iata": "VRN",
  "name": "Verona Villafranca Valerio Catullo Airport"
 },
 {
  "cc": "IT",
  "lat": "45.505299",
  "lon": "12.3519",
  "iata": "VCE",
  "name": "Venice Marco Polo Airport"
 },
 {
  "cc": "IT",
  "lat": "41.804532",
  "lon": "12.251998",
  "iata": "FCO",
  "name": "Rome\u2013Fiumicino Leonardo da Vinci International Airport"
 },
 {
  "cc": "IT",
  "lat": "40.886002",
  "lon": "14.2908",
  "iata": "NAP",
  "name": "Naples International Airport"
 },
 {
  "cc": "IT",
  "lat": "43.683899",
  "lon": "10.3927",
  "iata": "PSA",
  "name": "Pisa International Airport"
 },
 {
  "cc": "SI",
  "lat": "46.223701",
  "lon": "14.4576",
  "iata": "LJU",
  "name": "Ljubljana Jo\u017ee Pu\u010dnik Airport"
 },
 {
  "cc": "CZ",
  "lat": "50.100874",
  "lon": "14.259911",
  "iata": "PRG",
  "name": "V\u00e1clav Havel Airport Prague"
 },
 {
  "cc": "IL",
  "lat": "32.011398",
  "lon": "34.8867",
  "iata": "TLV",
  "name": "Ben Gurion International Airport"
 },
 {
  "cc": "IL",
  "lat": "29.727009",
  "lon": "35.014116",
  "iata": "ETM",
  "name": "Ramon International Airport"
 },
 {
  "cc": "MT",
  "lat": "35.857498",
  "lon": "14.4775",
  "iata": "MLA",
  "name": "Malta International Airport"
 },
 {
  "cc": "AT",
  "lat": "48.110298",
  "lon": "16.5697",
  "iata": "VIE",
  "name": "Vienna International Airport"
 },
 {
  "cc": "PT",
  "lat": "37.0144004822",
  "lon": "-7.96590995789",
  "iata": "FAO",
  "name": "Faro Airport"
 },
 {
  "cc": "PT",
  "lat": "32.697899",
  "lon": "-16.7745",
  "iata": "FNC",
  "name": "Madeira International Airport Cristiano Ronaldo"
 },
 {
  "cc": "PT",
  "lat": "37.7411994934",
  "lon": "-25.6979007721",
  "iata": "PDL",
  "name": "Jo\u00e3o Paulo II Airport"
 },
 {
  "cc": "PT",
  "lat": "41.2481002808",
  "lon": "-8.68138980865",
  "iata": "OPO",
  "name": "Francisco de S\u00e1 Carneiro Airport"
 },
 {
  "cc": "PT",
  "lat": "38.7813",
  "lon": "-9.13592",
  "iata": "LIS",
  "name": "Humberto Delgado Airport (Lisbon Portela Airport)"
 },
 {
  "cc": "RO",
  "lat": "44.572127",
  "lon": "26.103396",
  "iata": "OTP",
  "name": "Bucharest Henri Coand\u0103 International Airport"
 },
 {
  "cc": "CH",
  "lat": "46.238098",
  "lon": "6.10895",
  "iata": "GVA",
  "name": "Geneva Cointrin International Airport"
 },
 {
  "cc": "CH",
  "lat": "47.458056",
  "lon": "8.548056",
  "iata": "ZRH",
  "name": "Z\u00fcrich Airport"
 },
 {
  "cc": "TR",
  "lat": "40.128101",
  "lon": "32.995098",
  "iata": "ESB",
  "name": "Esenbo\u011fa International Airport"
 },
 {
  "cc": "TR",
  "lat": "36.898701",
  "lon": "30.800501",
  "iata": "AYT",
  "name": "Antalya International Airport"
 },
 {
  "cc": "TR",
  "lat": "40.971913",
  "lon": "28.823714",
  "iata": "ISL",
  "name": "\u0130stanbul Atat\u00fcrk Airport"
 },
 {
  "cc": "TR",
  "lat": "38.2924",
  "lon": "27.157",
  "iata": "ADB",
  "name": "Adnan Menderes International Airport"
 },
 {
  "cc": "TR",
  "lat": "36.7131004333",
  "lon": "28.7924995422",
  "iata": "DLM",
  "name": "Dalaman International Airport"
 },
 {
  "cc": "TR",
  "lat": "37.250599",
  "lon": "27.664301",
  "iata": "BJV",
  "name": "Milas Bodrum International Airport"
 },
 {
  "cc": "TR",
  "lat": "40.898602",
  "lon": "29.3092",
  "iata": "SAW",
  "name": "Istanbul Sabiha G\u00f6k\u00e7en International Airport"
 },
 {
  "cc": "TR",
  "lat": "41.261297",
  "lon": "28.741951",
  "iata": "IST",
  "name": "\u0130stanbul Airport"
 },
 {
  "cc": "MK",
  "lat": "41.958087",
  "lon": "21.622581",
  "iata": "SKP",
  "name": "Skopje International Airport"
 },
 {
  "cc": "RS",
  "lat": "44.818401",
  "lon": "20.309099",
  "iata": "BEG",
  "name": "Belgrade Nikola Tesla Airport"
 },
 {
  "cc": "ME",
  "lat": "42.359402",
  "lon": "19.2519",
  "iata": "TGD",
  "name": "Podgorica Airport / Podgorica Golubovci Airbase"
 },
 {
  "cc": "SK",
  "lat": "48.1702",
  "lon": "17.2127",
  "iata": "BTS",
  "name": "M. R. \u0160tef\u00e1nik Airport"
 },
 {
  "cc": "TC",
  "lat": "21.773697",
  "lon": "-72.268321",
  "iata": "PLS",
  "name": "Providenciales International Airport"
 },
 {
  "cc": "DO",
  "lat": "18.5674",
  "lon": "-68.363403",
  "iata": "PUJ",
  "name": "Punta Cana International Airport"
 },
 {
  "cc": "DO",
  "lat": "18.42970085144",
  "lon": "-69.668899536133",
  "iata": "SDQ",
  "name": "Las Am\u00e9ricas International Airport"
 },
 {
  "cc": "GT",
  "lat": "14.5833",
  "lon": "-90.527496",
  "iata": "GUA",
  "name": "La Aurora Airport"
 },
 {
  "cc": "JM",
  "lat": "17.935699462890625",
  "lon": "-76.7874984741211",
  "iata": "KIN",
  "name": "Norman Manley International Airport"
 },
 {
  "cc": "MX",
  "lat": "20.511425",
  "lon": "-86.930287",
  "iata": "CZM",
  "name": "Aeropuerto Internacional de Cozumel"
 },
 {
  "cc": "MX",
  "lat": "24.125908",
  "lon": "-104.533904",
  "iata": "DGO",
  "name": "Aeropuerto Internacional Gral, Guadalupe Victoria"
 },
 {
  "cc": "MX",
  "lat": "20.523342",
  "lon": "-103.310108",
  "iata": "GDL",
  "name": "Aeropuerto Internacional Miguel Hidalgo"
 },
 {
  "cc": "MX",
  "lat": "20.933384",
  "lon": "-89.662621",
  "iata": "MID",
  "name": "Aeropuerto Internacional Manuel Crescencio Rej\u00f3n"
 },
 {
  "cc": "MX",
  "lat": "19.435433",
  "lon": "-99.082432",
  "iata": "MEX",
  "name": "Aeropuerto Internacional Lic. Benito Ju\u00e1rez"
 },
 {
  "cc": "MX",
  "lat": "25.778521",
  "lon": "-100.106989",
  "iata": "MTY",
  "name": "Monterrey International Airport"
 },
 {
  "cc": "MX",
  "lat": "23.161474",
  "lon": "-106.264572",
  "iata": "MZT",
  "name": "General Rafael Buelna International Airport"
 },
 {
  "cc": "MX",
  "lat": "20.679746",
  "lon": "-105.246685",
  "iata": "PVR",
  "name": "Aeropuerto Internacional Lic. Gustavo D\u00edaz Ordaz"
 },
 {
  "cc": "MX",
  "lat": "23.151919",
  "lon": "-109.720731",
  "iata": "SJD",
  "name": "Aeropuerto Internacional de Los Cabos"
 },
 {
  "cc": "MX",
  "lat": "30.931996",
  "lon": "-114.80847",
  "iata": "SFH",
  "name": "Aeropuerto Internacional San Felipe"
 },
 {
  "cc": "MX",
  "lat": "19.7357",
  "lon": "-99.0257",
  "iata": "NLU",
  "name": "Aeropuerto Internacional General Felipe \u00c1ngeles"
 },
 {
  "cc": "MX",
  "lat": "32.545963",
  "lon": "-116.975856",
  "iata": "TIJ",
  "name": "Aeropuerto Internacional Gral. Abelardo Rodriguez"
 },
 {
  "cc": "MX",
  "lat": "21.039444",
  "lon": "-86.874304",
  "iata": "CUN",
  "name": "Aeropuerto Internacional de Canc\u00fan"
 },
 {
  "cc": "PA",
  "lat": "9.07136",
  "lon": "-79.383499",
  "iata": "PTY",
  "name": "Tocumen International Airport"
 },
 {
  "cc": "CR",
  "lat": "10.5933",
  "lon": "-85.544403",
  "iata": "LIR",
  "name": "Guanacaste Airport"
 },
 {
  "cc": "SV",
  "lat": "13.4409",
  "lon": "-89.055702",
  "iata": "SAL",
  "name": "Monse\u00f1or \u00d3scar Arnulfo Romero International Airport"
 },
 {
  "cc": "HT",
  "lat": "18.58",
  "lon": "-72.292503",
  "iata": "PAP",
  "name": "Toussaint Louverture International Airport"
 },
 {
  "cc": "CU",
  "lat": "22.989200592041016",
  "lon": "-82.40910339355469",
  "iata": "HAV",
  "name": "Jos\u00e9 Mart\u00ed International Airport"
 },
 {
  "cc": "CU",
  "lat": "23.034401",
  "lon": "-81.435303",
  "iata": "VRA",
  "name": "Juan Gualberto Gomez International Airport"
 },
 {
  "cc": "KY",
  "lat": "19.292801",
  "lon": "-81.357697",
  "iata": "GCM",
  "name": "Owen Roberts International Airport"
 },
 {
  "cc": "MX",
  "lat": "0.031",
  "lon": "0.011",
  "iata": "",
  "name": "(Duplicate)Aeropuerto Internacional Gral. Alberto Salinas Carranza"
 },
 {
  "cc": "BS",
  "lat": "25.039",
  "lon": "-77.466202",
  "iata": "NAS",
  "name": "Lynden Pindling International Airport"
 },
 {
  "cc": "BZ",
  "lat": "17.539951",
  "lon": "-88.303556",
  "iata": "BZE",
  "name": "Philip S. W. Goldson International Airport"
 },
 {
  "cc": "PF",
  "lat": "-17.553699",
  "lon": "-149.606995",
  "iata": "PPT",
  "name": "Faa'a International Airport"
 },
 {
  "cc": "VU",
  "lat": "-17.699301",
  "lon": "168.320007",
  "iata": "VLI",
  "name": "Bauerfield International Airport"
 },
 {
  "cc": "NZ",
  "lat": "-37.01199",
  "lon": "174.786331",
  "iata": "AKL",
  "name": "Auckland International Airport"
 },
 {
  "cc": "NZ",
  "lat": "-43.48939895629883",
  "lon": "172.53199768066406",
  "iata": "CHC",
  "name": "Christchurch International Airport"
 },
 {
  "cc": "NZ",
  "lat": "-41.3272018433",
  "lon": "174.804992676",
  "iata": "WLG",
  "name": "Wellington International Airport"
 },
 {
  "cc": "BH",
  "lat": "26.267295",
  "lon": "50.63764",
  "iata": "BAH",
  "name": "Bahrain International Airport"
 },
 {
  "cc": "SA",
  "lat": "26.471201",
  "lon": "49.797901",
  "iata": "DMM",
  "name": "King Fahd International Airport"
 },
 {
  "cc": "SA",
  "lat": "26.2654",
  "lon": "50.152",
  "iata": "DHA",
  "name": "King Abdulaziz Air Base"
 },
 {
  "cc": "SA",
  "lat": "21.6796",
  "lon": "39.156502",
  "iata": "JED",
  "name": "King Abdulaziz International Airport"
 },
 {
  "cc": "SA",
  "lat": "24.5534",
  "lon": "39.705101",
  "iata": "MED",
  "name": "Prince Mohammad Bin Abdulaziz Airport"
 },
 {
  "cc": "SA",
  "lat": "24.9576",
  "lon": "46.698799",
  "iata": "RUH",
  "name": "King Khaled International Airport"
 },
 {
  "cc": "IR",
  "lat": "35.416099548339844",
  "lon": "51.152198791503906",
  "iata": "IKA",
  "name": "Imam Khomeini International Airport"
 },
 {
  "cc": "IR",
  "lat": "35.68920135498047",
  "lon": "51.31340026855469",
  "iata": "THR",
  "name": "Mehrabad International Airport"
 },
 {
  "cc": "IR",
  "lat": "36.235198974609375",
  "lon": "59.64099884033203",
  "iata": "MHD",
  "name": "Mashhad International Airport"
 },
 {
  "cc": "IR",
  "lat": "29.5392",
  "lon": "52.589802",
  "iata": "SYZ",
  "name": "Shiraz Shahid Dastghaib International Airport"
 },
 {
  "cc": "JO",
  "lat": "31.7226009369",
  "lon": "35.9931983948",
  "iata": "AMM",
  "name": "Queen Alia International Airport"
 },
 {
  "cc": "KW",
  "lat": "29.226601",
  "lon": "47.968899",
  "iata": "KWI",
  "name": "Kuwait International Airport"
 },
 {
  "cc": "LB",
  "lat": "33.820899963378906",
  "lon": "35.488399505615234",
  "iata": "BEY",
  "name": "Beirut Rafic Hariri International Airport"
 },
 {
  "cc": "OM",
  "lat": "19.501944",
  "lon": "57.634167",
  "iata": "DQM",
  "name": "Duqm International Airport"
 },
 {
  "cc": "AE",
  "lat": "24.443764",
  "lon": "54.651718",
  "iata": "AUH",
  "name": "Abu Dhabi International Airport"
 },
 {
  "cc": "AE",
  "lat": "25.2527999878",
  "lon": "55.3643989563",
  "iata": "DXB",
  "name": "Dubai International Airport"
 },
 {
  "cc": "AE",
  "lat": "24.896356",
  "lon": "55.161389",
  "iata": "DWC",
  "name": "Al Maktoum International Airport"
 },
 {
  "cc": "AE",
  "lat": "25.3286",
  "lon": "55.5172",
  "iata": "SHJ",
  "name": "Sharjah International Airport"
 },
 {
  "cc": "OM",
  "lat": "23.5933",
  "lon": "58.284401",
  "iata": "MCT",
  "name": "Muscat International Airport"
 },
 {
  "cc": "PK",
  "lat": "33.549",
  "lon": "72.82566",
  "iata": "ISB",
  "name": "Islamabad International Airport"
 },
 {
  "cc": "PK",
  "lat": "24.9065",
  "lon": "67.160797",
  "iata": "KHI",
  "name": "Jinnah International Airport"
 },
 {
  "cc": "PK",
  "lat": "31.521601",
  "lon": "74.403603",
  "iata": "LHE",
  "name": "Allama Iqbal International Airport"
 },
 {
  "cc": "IQ",
  "lat": "33.262501",
  "lon": "44.2346",
  "iata": "BGW",
  "name": "Baghdad International Airport / New Al Muthana Air Base"
 },
 {
  "cc": "SY",
  "lat": "33.4114990234375",
  "lon": "36.51559829711914",
  "iata": "DAM",
  "name": "Damascus International Airport"
 },
 {
  "cc": "QA",
  "lat": "25.273056",
  "lon": "51.608056",
  "iata": "DOH",
  "name": "Hamad International Airport"
 },
 {
  "cc": "US",
  "lat": "61.179004",
  "lon": "-149.992561",
  "iata": "ANC",
  "name": "Ted Stevens Anchorage International Airport"
 },
 {
  "cc": "GU",
  "lat": "13.4834",
  "lon": "144.796005",
  "iata": "GUM",
  "name": "Antonio B. Won Pat International Airport"
 },
 {
  "cc": "US",
  "lat": "21.32062",
  "lon": "-157.924228",
  "iata": "HNL",
  "name": "Daniel K Inouye International Airport"
 },
 {
  "cc": "US",
  "lat": "20.896263",
  "lon": "-156.431837",
  "iata": "OGG",
  "name": "Kahului International Airport"
 },
 {
  "cc": "TW",
  "lat": "22.577101",
  "lon": "120.349998",
  "iata": "KHH",
  "name": "Kaohsiung International Airport"
 },
 {
  "cc": "TW",
  "lat": "25.0777",
  "lon": "121.233002",
  "iata": "TPE",
  "name": "Taiwan Taoyuan International Airport"
 },
 {
  "cc": "JP",
  "lat": "35.764702",
  "lon": "140.386002",
  "iata": "NRT",
  "name": "Narita International Airport"
 },
 {
  "cc": "JP",
  "lat": "34.427299",
  "lon": "135.244003",
  "iata": "KIX",
  "name": "Kansai International Airport"
 },
 {
  "cc": "JP",
  "lat": "42.7752",
  "lon": "141.692001",
  "iata": "CTS",
  "name": "New Chitose Airport"
 },
 {
  "cc": "JP",
  "lat": "33.585899353027344",
  "lon": "130.4510040283203",
  "iata": "FUK",
  "name": "Fukuoka Airport"
 },
 {
  "cc": "JP",
  "lat": "31.8034",
  "lon": "130.718994",
  "iata": "KOJ",
  "name": "Kagoshima Airport"
 },
 {
  "cc": "JP",
  "lat": "34.858398",
  "lon": "136.804993",
  "iata": "NGO",
  "name": "Chubu Centrair International Airport"
 },
 {
  "cc": "JP",
  "lat": "34.7855",
  "lon": "135.438004",
  "iata": "ITM",
  "name": "Osaka International Airport"
 },
 {
  "cc": "JP",
  "lat": "38.139702",
  "lon": "140.917007",
  "iata": "SDJ",
  "name": "Sendai Airport"
 },
 {
  "cc": "JP",
  "lat": "35.552299",
  "lon": "139.779999",
  "iata": "HND",
  "name": "Tokyo Haneda International Airport"
 },
 {
  "cc": "JP",
  "lat": "35.748501",
  "lon": "139.348007",
  "iata": "OKO",
  "name": "Yokota Air Base"
 },
 {
  "cc": "KR",
  "lat": "34.991406",
  "lon": "126.382814",
  "iata": "MWX",
  "name": "Muan International Airport"
 },
 {
  "cc": "KR",
  "lat": "33.512058",
  "lon": "126.492548",
  "iata": "CJU",
  "name": "Jeju International Airport"
 },
 {
  "cc": "KR",
  "lat": "35.179501",
  "lon": "128.938004",
  "iata": "PUS",
  "name": "Gimhae International Airport"
 },
 {
  "cc": "KR",
  "lat": "37.469101",
  "lon": "126.450996",
  "iata": "ICN",
  "name": "Incheon International Airport"
 },
 {
  "cc": "KR",
  "lat": "37.5583",
  "lon": "126.791",
  "iata": "GMP",
  "name": "Gimpo International Airport"
 },
 {
  "cc": "JP",
  "lat": "26.195801",
  "lon": "127.646004",
  "iata": "OKA",
  "name": "Naha Airport / JASDF Naha Air Base"
 },
 {
  "cc": "JP",
  "lat": "26.351667",
  "lon": "127.769444",
  "iata": "DNA",
  "name": "Kadena Air Base"
 },
 {
  "cc": "PH",
  "lat": "14.5086",
  "lon": "121.019997",
  "iata": "MNL",
  "name": "Ninoy Aquino International Airport"
 },
 {
  "cc": "PH",
  "lat": "7.12552",
  "lon": "125.646004",
  "iata": "DVO",
  "name": "Francisco Bangoy International Airport"
 },
 {
  "cc": "PH",
  "lat": "10.309261",
  "lon": "123.97974",
  "iata": "CEB",
  "name": "Mactan Cebu International Airport"
 },
 {
  "cc": "RU",
  "lat": "52.634998",
  "lon": "39.445",
  "iata": "",
  "name": "Lipetsk Air Base"
 },
 {
  "cc": "AR",
  "lat": "-34.5592",
  "lon": "-58.4156",
  "iata": "AEP",
  "name": "Jorge Newbery Airpark"
 },
 {
  "cc": "AR",
  "lat": "-34.8222",
  "lon": "-58.5358",
  "iata": "EZE",
  "name": "Minister Pistarini International Airport"
 },
 {
  "cc": "BR",
  "lat": "-1.379279",
  "lon": "-48.476207",
  "iata": "BEL",
  "name": "Val de Cans/J\u00falio Cezar Ribeiro International Airport"
 },
 {
  "cc": "BR",
  "lat": "-15.869167",
  "lon": "-47.920834",
  "iata": "BSB",
  "name": "Presidente Juscelino Kubitschek International Airport"
 },
 {
  "cc": "BR",
  "lat": "-19.63571",
  "lon": "-43.966928",
  "iata": "CNF",
  "name": "Tancredo Neves International Airport"
 },
 {
  "cc": "BR",
  "lat": "-3.03861",
  "lon": "-60.049702",
  "iata": "MAO",
  "name": "Eduardo Gomes International Airport"
 },
 {
  "cc": "BR",
  "lat": "-27.670279",
  "lon": "-48.552502",
  "iata": "FLN",
  "name": "Herc\u00edlio Luz International Airport"
 },
 {
  "cc": "BR",
  "lat": "-3.775833",
  "lon": "-38.532222",
  "iata": "FOR",
  "name": "Pinto Martins International Airport"
 },
 {
  "cc": "BR",
  "lat": "-22.809999",
  "lon": "-43.250557",
  "iata": "GIG",
  "name": "Rio Gale\u00e3o \u2013 Tom Jobim International Airport"
 },
 {
  "cc": "BR",
  "lat": "-23.431944",
  "lon": "-46.467778",
  "iata": "GRU",
  "name": "Guarulhos - Governador Andr\u00e9 Franco Montoro International Airport"
 },
 {
  "cc": "BR",
  "lat": "-16.438426",
  "lon": "-39.080584",
  "iata": "BPS",
  "name": "Porto Seguro Airport"
 },
 {
  "cc": "BR",
  "lat": "-12.908611",
  "lon": "-38.322498",
  "iata": "SSA",
  "name": "Deputado Luiz Eduardo Magalh\u00e3es International Airport"
 },
 {
  "cc": "BR",
  "lat": "-20.258",
  "lon": "-40.285",
  "iata": "VIX",
  "name": "Eurico de Aguiar Salles Airport"
 },
 {
  "cc": "CL",
  "lat": "-33.393001556396484",
  "lon": "-70.78579711914062",
  "iata": "SCL",
  "name": "Comodoro Arturo Merino Ben\u00edtez International Airport"
 },
 {
  "cc": "EC",
  "lat": "-2.15742",
  "lon": "-79.883598",
  "iata": "GYE",
  "name": "Jos\u00e9 Joaqu\u00edn de Olmedo International Airport"
 },
 {
  "cc": "EC",
  "lat": "-0.125399",
  "lon": "-78.354306",
  "iata": "UIO",
  "name": "Mariscal Sucre International Airport"
 },
 {
  "cc": "PY",
  "lat": "-25.240156",
  "lon": "-57.519227",
  "iata": "ASU",
  "name": "Aeropuerto Internacional Silvio Pettirossi"
 },
 {
  "cc": "PY",
  "lat": "-27.221691",
  "lon": "-55.833807",
  "iata": "ENO",
  "name": "Aeropuerto Internacional Tte. Amin Ayub Gonz\u00e1lez"
 },
 {
  "cc": "PY",
  "lat": "-25.457186",
  "lon": "-54.839544",
  "iata": "AGT",
  "name": "Aeropuerto Internacional Guaran\u00ed"
 },
 {
  "cc": "PY",
  "lat": "-22.033912",
  "lon": "-60.618964",
  "iata": "ESG",
  "name": "Aeropuerto Internacional Dr. Luis Maria Arga\u00f1a"
 },
 {
  "cc": "PY",
  "lat": "-22.640946",
  "lon": "-55.832005",
  "iata": "PJC",
  "name": "Aeropuerto Internacional Dr. Augusto Roberto Fuster"
 },
 {
  "cc": "CO",
  "lat": "4.70159",
  "lon": "-74.1469",
  "iata": "BOG",
  "name": "El Dorado International Airport"
 },
 {
  "cc": "BO",
  "lat": "-17.6448",
  "lon": "-63.135399",
  "iata": "VVI",
  "name": "Viru Viru International Airport"
 },
 {
  "cc": "SR",
  "lat": "5.45283",
  "lon": "-55.187801",
  "iata": "PBM",
  "name": "Johan Adolf Pengel International Airport"
 },
 {
  "cc": "GF",
  "lat": "4.819964",
  "lon": "-52.361326",
  "iata": "CAY",
  "name": "Cayenne \u2013 F\u00e9lix Ebou\u00e9 Airport"
 },
 {
  "cc": "PE",
  "lat": "-12.0219",
  "lon": "-77.114305",
  "iata": "LIM",
  "name": "Jorge Ch\u00e1vez International Airport"
 },
 {
  "cc": "PE",
  "lat": "-13.535699844400002",
  "lon": "-71.9387969971",
  "iata": "CUZ",
  "name": "Alejandro Velasco Astete International Airport"
 },
 {
  "cc": "UY",
  "lat": "-34.835647",
  "lon": "-56.026497",
  "iata": "MVD",
  "name": "Carrasco General Ces\u00e1reo L. Berisso International Airport"
 },
 {
  "cc": "VE",
  "lat": "10.111111",
  "lon": "-64.692222",
  "iata": "BLA",
  "name": "General Jos\u00e9 Antonio Anzoategui International Airport"
 },
 {
  "cc": "VE",
  "lat": "10.601194",
  "lon": "-66.991222",
  "iata": "CCS",
  "name": "Sim\u00f3n Bol\u00edvar International Airport"
 },
 {
  "cc": "CN",
  "lat": "36.361953",
  "lon": "120.088171",
  "iata": "TAO",
  "name": "Qingdao Jiaodong International Airport"
 },
 {
  "cc": "MQ",
  "lat": "14.591",
  "lon": "-61.003201",
  "iata": "FDF",
  "name": "Martinique Aim\u00e9 C\u00e9saire International Airport"
 },
 {
  "cc": "GP",
  "lat": "16.265301",
  "lon": "-61.531799",
  "iata": "PTP",
  "name": "Pointe-\u00e0-Pitre Le Raizet International  Airport"
 },
 {
  "cc": "PR",
  "lat": "18.4394",
  "lon": "-66.001801",
  "iata": "SJU",
  "name": "Luis Munoz Marin International Airport"
 },
 {
  "cc": "LC",
  "lat": "13.7332",
  "lon": "-60.952599",
  "iata": "UVF",
  "name": "Hewanorra International Airport"
 },
 {
  "cc": "AW",
  "lat": "12.5014",
  "lon": "-70.015198",
  "iata": "AUA",
  "name": "Queen Beatrix International Airport"
 },
 {
  "cc": "BQ",
  "lat": "12.131",
  "lon": "-68.268501",
  "iata": "BON",
  "name": "Flamingo International Airport"
 },
 {
  "cc": "CW",
  "lat": "12.1889",
  "lon": "-68.959801",
  "iata": "CUR",
  "name": "Hato International Airport"
 },
 {
  "cc": "SX",
  "lat": "18.041",
  "lon": "-63.108898",
  "iata": "SXM",
  "name": "Princess Juliana International Airport"
 },
 {
  "cc": "TR",
  "lat": "36.890908",
  "lon": "35.070522",
  "iata": "COV",
  "name": "\u00c7ukurova International Airport (under construction)"
 },
 {
  "cc": "KZ",
  "lat": "43.354267",
  "lon": "77.042828",
  "iata": "ALA",
  "name": "Almaty International Airport"
 },
 {
  "cc": "KZ",
  "lat": "51.027035",
  "lon": "71.467094",
  "iata": "NQZ",
  "name": "Nursultan Nazarbayev International Airport"
 },
 {
  "cc": "KG",
  "lat": "43.0612983704",
  "lon": "74.4776000977",
  "iata": "FRU",
  "name": "Manas International Airport"
 },
 {
  "cc": "AZ",
  "lat": "40.467498779296875",
  "lon": "50.04669952392578",
  "iata": "GYD",
  "name": "Heydar Aliyev International Airport"
 },
 {
  "cc": "AM",
  "lat": "40.1473007202",
  "lon": "44.3959007263",
  "iata": "EVN",
  "name": "Zvartnots International Airport"
 },
 {
  "cc": "GE",
  "lat": "41.669201",
  "lon": "44.9547",
  "iata": "TBS",
  "name": "Tbilisi International Airport"
 },
 {
  "cc": "RU",
  "lat": "43.396256",
  "lon": "132.148155",
  "iata": "VVO",
  "name": "Vladivostok International Airport"
 },
 {
  "cc": "UA",
  "lat": "50.345001",
  "lon": "30.894699",
  "iata": "KBP",
  "name": "Boryspil International Airport"
 },
 {
  "cc": "UA",
  "lat": "49.8125",
  "lon": "23.9561",
  "iata": "LWO",
  "name": "Lviv International Airport"
 },
 {
  "cc": "RU",
  "lat": "59.800301",
  "lon": "30.262501",
  "iata": "LED",
  "name": "Pulkovo Airport"
 },
 {
  "cc": "BY",
  "lat": "53.888071",
  "lon": "28.039964",
  "iata": "MSQ",
  "name": "Minsk National Airport"
 },
 {
  "cc": "RU",
  "lat": "56.173077",
  "lon": "92.492437",
  "iata": "KJA",
  "name": "Krasnoyarsk International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.019756",
  "lon": "82.618675",
  "iata": "OVB",
  "name": "Novosibirsk Tolmachevo Airport"
 },
 {
  "cc": "RU",
  "lat": "47.493888",
  "lon": "39.924722",
  "iata": "ROV",
  "name": "Platov International Airport"
 },
 {
  "cc": "RU",
  "lat": "43.449902",
  "lon": "39.9566",
  "iata": "AER",
  "name": "Sochi International Airport"
 },
 {
  "cc": "RU",
  "lat": "56.743099212646",
  "lon": "60.802700042725",
  "iata": "SVX",
  "name": "Koltsovo Airport"
 },
 {
  "cc": "TM",
  "lat": "37.986801",
  "lon": "58.361",
  "iata": "ASB",
  "name": "Ashgabat International Airport"
 },
 {
  "cc": "UZ",
  "lat": "41.257900238",
  "lon": "69.2811965942",
  "iata": "TAS",
  "name": "Tashkent International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.553299",
  "lon": "38.150002",
  "iata": "ZIA",
  "name": "Zhukovsky International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.408798",
  "lon": "37.9063",
  "iata": "DME",
  "name": "Domodedovo International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.972599",
  "lon": "37.4146",
  "iata": "SVO",
  "name": "Sheremetyevo International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.591499",
  "lon": "37.261501",
  "iata": "VKO",
  "name": "Vnukovo International Airport"
 },
 {
  "cc": "RU",
  "lat": "55.606201171875",
  "lon": "49.278701782227",
  "iata": "KZN",
  "name": "Kazan International Airport"
 },
 {
  "cc": "RU",
  "lat": "51.712778",
  "lon": "46.171111",
  "iata": "GSV",
  "name": "Gagarin International Airport"
 },
 {
  "cc": "RU",
  "lat": "54.557498931885",
  "lon": "55.874401092529",
  "iata": "UFA",
  "name": "Ufa International Airport"
 },
 {
  "cc": "RU",
  "lat": "53.504902",
  "lon": "50.164299",
  "iata": "KUF",
  "name": "Kurumoch International Airport"
 },
 {
  "cc": "IN",
  "lat": "19.0886993408",
  "lon": "72.8678970337",
  "iata": "BOM",
  "name": "Chhatrapati Shivaji International Airport"
 },
 {
  "cc": "IN",
  "lat": "15.3808",
  "lon": "73.831398",
  "iata": "GOI",
  "name": "Dabolim Airport"
 },
 {
  "cc": "IN",
  "lat": "22.378824",
  "lon": "71.039391",
  "iata": "HSR",
  "name": "Rajkot International Airport"
 },
 {
  "cc": "LK",
  "lat": "7.180759906768799",
  "lon": "79.88410186767578",
  "iata": "CMB",
  "name": "Bandaranaike International Colombo Airport"
 },
 {
  "cc": "LK",
  "lat": "6.284467",
  "lon": "81.124128",
  "iata": "HRI",
  "name": "Mattala Rajapaksa International Airport"
 },
 {
  "cc": "KH",
  "lat": "11.5466",
  "lon": "104.844002",
  "iata": "PNH",
  "name": "Phnom Penh International Airport"
 },
 {
  "cc": "KH",
  "lat": "13.369167",
  "lon": "104.223056",
  "iata": "SAI",
  "name": "Siem Reap-Angkor International Airport"
 },
 {
  "cc": "IN",
  "lat": "0.02675",
  "lon": "0.00821",
  "iata": "",
  "name": "(Duplicate}Maharishi Valmiki International Airport"
 },
 {
  "cc": "IN",
  "lat": "22.654699",
  "lon": "88.446701",
  "iata": "CCU",
  "name": "Netaji Subhash Chandra Bose International Airport"
 },
 {
  "cc": "BD",
  "lat": "23.843347",
  "lon": "90.397783",
  "iata": "DAC",
  "name": "Hazrat Shahjalal International Airport"
 },
 {
  "cc": "HK",
  "lat": "22.308901",
  "lon": "113.915001",
  "iata": "HKG",
  "name": "Hong Kong International Airport"
 },
 {
  "cc": "IN",
  "lat": "28.55563",
  "lon": "77.09519",
  "iata": "DEL",
  "name": "Indira Gandhi International Airport"
 },
 {
  "cc": "MO",
  "lat": "22.149599",
  "lon": "113.592003",
  "iata": "MFM",
  "name": "Macau International Airport"
 },
 {
  "cc": "VN",
  "lat": "0.01",
  "lon": "0.01",
  "iata": "",
  "name": "(SPAM)fun88family"
 },
 {
  "cc": "NP",
  "lat": "27.6966",
  "lon": "85.3591",
  "iata": "KTM",
  "name": "Tribhuvan International Airport"
 },
 {
  "cc": "IN",
  "lat": "13.1979",
  "lon": "77.706299",
  "iata": "BLR",
  "name": "Kempegowda International Airport"
 },
 {
  "cc": "IN",
  "lat": "10.152",
  "lon": "76.401901",
  "iata": "COK",
  "name": "Cochin International Airport"
 },
 {
  "cc": "IN",
  "lat": "17.231318",
  "lon": "78.429855",
  "iata": "HYD",
  "name": "Rajiv Gandhi International Airport"
 },
 {
  "cc": "IN",
  "lat": "12.990005",
  "lon": "80.169296",
  "iata": "MAA",
  "name": "Chennai International Airport"
 },
 {
  "cc": "IN",
  "lat": "8.48212",
  "lon": "76.920097",
  "iata": "TRV",
  "name": "Thiruvananthapuram International Airport"
 },
 {
  "cc": "MV",
  "lat": "4.191830158233643",
  "lon": "73.52909851074219",
  "iata": "MLE",
  "name": "Mal\u00e9 International Airport"
 },
 {
  "cc": "TH",
  "lat": "13.9125995636",
  "lon": "100.607002258",
  "iata": "DMK",
  "name": "Don Mueang International Airport"
 },
 {
  "cc": "TH",
  "lat": "13.681099891662598",
  "lon": "100.74700164794922",
  "iata": "BKK",
  "name": "Suvarnabhumi Airport"
 },
 {
  "cc": "TH",
  "lat": "18.766799926799997",
  "lon": "98.962600708",
  "iata": "CNX",
  "name": "Chiang Mai International Airport"
 },
 {
  "cc": "TH",
  "lat": "8.1132",
  "lon": "98.316902",
  "iata": "HKT",
  "name": "Phuket International Airport"
 },
 {
  "cc": "VN",
  "lat": "21.221201",
  "lon": "105.806999",
  "iata": "HAN",
  "name": "Noi Bai International Airport"
 },
 {
  "cc": "VN",
  "lat": "10.8188",
  "lon": "106.652",
  "iata": "SGN",
  "name": "Tan Son Nhat International Airport"
 },
 {
  "cc": "MM",
  "lat": "21.702199935913086",
  "lon": "95.97789764404297",
  "iata": "MDL",
  "name": "Mandalay International Airport"
 },
 {
  "cc": "MM",
  "lat": "16.907300949099998",
  "lon": "96.1332015991",
  "iata": "RGN",
  "name": "Yangon International Airport"
 },
 {
  "cc": "ID",
  "lat": "-5.06163",
  "lon": "119.554001",
  "iata": "UPG",
  "name": "Hasanuddin International Airport"
 },
 {
  "cc": "ID",
  "lat": "-8.74817",
  "lon": "115.167",
  "iata": "DPS",
  "name": "Ngurah Rai (Bali) International Airport"
 },
 {
  "cc": "ID",
  "lat": "-2.579627",
  "lon": "140.519857",
  "iata": "DJJ",
  "name": "Dortheys Hiyo Eluay International Airport"
 },
 {
  "cc": "ID",
  "lat": "-1.268342",
  "lon": "116.89452",
  "iata": "BPN",
  "name": "Sultan Aji Muhammad Sulaiman Sepinggan International Airport"
 },
 {
  "cc": "ID",
  "lat": "-7.37983",
  "lon": "112.787003",
  "iata": "SUB",
  "name": "Juanda International Airport"
 },
 {
  "cc": "BN",
  "lat": "4.9442",
  "lon": "114.928001",
  "iata": "BWN",
  "name": "Brunei International Airport"
 },
 {
  "cc": "ID",
  "lat": "-6.1255698204",
  "lon": "106.65599823",
  "iata": "CGK",
  "name": "Soekarno-Hatta International Airport"
 },
 {
  "cc": "ID",
  "lat": "3.637847",
  "lon": "98.870566",
  "iata": "KNO",
  "name": "Kualanamu International Airport"
 },
 {
  "cc": "MY",
  "lat": "2.74558",
  "lon": "101.709999",
  "iata": "KUL",
  "name": "Kuala Lumpur International Airport"
 },
 {
  "cc": "SG",
  "lat": "1.35019",
  "lon": "103.994003",
  "iata": "SIN",
  "name": "Singapore Changi Airport"
 },
 {
  "cc": "AU",
  "lat": "-27.384199142456055",
  "lon": "153.11700439453125",
  "iata": "BNE",
  "name": "Brisbane International Airport"
 },
 {
  "cc": "AU",
  "lat": "-37.673302",
  "lon": "144.843002",
  "iata": "MEL",
  "name": "Melbourne International Airport"
 },
 {
  "cc": "CN",
  "lat": "37.659724",
  "lon": "120.978124",
  "iata": "YNT",
  "name": "Yantai Penglai International Airport"
 },
 {
  "cc": "AU",
  "lat": "-34.947512",
  "lon": "138.533393",
  "iata": "ADL",
  "name": "Adelaide International Airport"
 },
 {
  "cc": "AU",
  "lat": "-12.41497",
  "lon": "130.88185",
  "iata": "DRW",
  "name": "Darwin International Airport / RAAF Darwin"
 },
 {
  "cc": "AU",
  "lat": "-31.94029998779297",
  "lon": "115.96700286865234",
  "iata": "PER",
  "name": "Perth International Airport"
 },
 {
  "cc": "AU",
  "lat": "-33.94609832763672",
  "lon": "151.177001953125",
  "iata": "SYD",
  "name": "Sydney Kingsford Smith International Airport"
 },
 {
  "cc": "CN",
  "lat": "40.080101013183594",
  "lon": "116.58499908447266",
  "iata": "PEK",
  "name": "Beijing Capital International Airport"
 },
 {
  "cc": "CN",
  "lat": "39.509945",
  "lon": "116.41092",
  "iata": "PKX",
  "name": "Beijing Daxing International Airport"
 },
 {
  "cc": "CN",
  "lat": "40.849658",
  "lon": "111.824598",
  "iata": "HET",
  "name": "Hohhot Baita International Airport"
 },
 {
  "cc": "CN",
  "lat": "39.124401092499994",
  "lon": "117.346000671",
  "iata": "TSN",
  "name": "Tianjin Binhai International Airport"
 },
 {
  "cc": "CN",
  "lat": "37.746899",
  "lon": "112.627998",
  "iata": "TYN",
  "name": "Taiyuan Wusu Airport"
 },
 {
  "cc": "CN",
  "lat": "23.392401",
  "lon": "113.299004",
  "iata": "CAN",
  "name": "Guangzhou Baiyun International Airport"
 },
 {
  "cc": "CN",
  "lat": "28.189199",
  "lon": "113.220001",
  "iata": "CSX",
  "name": "Changsha Huanghua International Airport"
 },
 {
  "cc": "CN",
  "lat": "25.219828",
  "lon": "110.039553",
  "iata": "KWL",
  "name": "Guilin Liangjiang International Airport"
 },
 {
  "cc": "CN",
  "lat": "22.608299",
  "lon": "108.171997",
  "iata": "NNG",
  "name": "Nanning Wuxu Airport"
 },
 {
  "cc": "CN",
  "lat": "22.639299",
  "lon": "113.810997",
  "iata": "SZX",
  "name": "Shenzhen Bao'an International Airport"
 },
 {
  "cc": "CN",
  "lat": "34.526497",
  "lon": "113.849165",
  "iata": "CGO",
  "name": "Zhengzhou Xinzheng International Airport"
 },
 {
  "cc": "CN",
  "lat": "30.774798",
  "lon": "114.213723",
  "iata": "WUH",
  "name": "Wuhan Tianhe International Airport"
 },
 {
  "cc": "CN",
  "lat": "19.9349",
  "lon": "110.459",
  "iata": "HAK",
  "name": "Haikou Meilan International Airport"
 },
 {
  "cc": "CN",
  "lat": "18.3029",
  "lon": "109.412003",
  "iata": "SYX",
  "name": "Sanya Phoenix International Airport"
 },
 {
  "cc": "CN",
  "lat": "36.515202",
  "lon": "103.620003",
  "iata": "LHW",
  "name": "Lanzhou Zhongchuan International Airport"
 },
 {
  "cc": "CN",
  "lat": "34.447102",
  "lon": "108.751999",
  "iata": "XIY",
  "name": "Xi'an Xianyang International Airport"
 },
 {
  "cc": "MN",
  "lat": "47.646916",
  "lon": "106.819833",
  "iata": "UBN",
  "name": "Ulaanbaatar Chinggis Khaan International Airport"
 },
 {
  "cc": "CN",
  "lat": "25.110313",
  "lon": "102.936743",
  "iata": "KMG",
  "name": "Kunming Changshui International Airport"
 },
 {
  "cc": "CN",
  "lat": "24.54400062561035",
  "lon": "118.12799835205078",
  "iata": "XMN",
  "name": "Xiamen Gaoqi International Airport"
 },
 {
  "cc": "CN",
  "lat": "28.864815",
  "lon": "115.90271",
  "iata": "KHN",
  "name": "Nanchang Changbei International Airport"
 },
 {
  "cc": "CN",
  "lat": "25.934669",
  "lon": "119.66318",
  "iata": "FOC",
  "name": "Fuzhou Changle International Airport"
 },
 {
  "cc": "CN",
  "lat": "30.23609",
  "lon": "120.428865",
  "iata": "HGH",
  "name": "Hangzhou Xiaoshan International Airport"
 },
 {
  "cc": "CN",
  "lat": "36.857201",
  "lon": "117.216003",
  "iata": "TNA",
  "name": "Jinan Yaoqiang International Airport"
 },
 {
  "cc": "CN",
  "lat": "29.82670021057129",
  "lon": "121.46199798583984",
  "iata": "NGB",
  "name": "Ningbo Lishe International Airport"
 },
 {
  "cc": "CN",
  "lat": "31.735032",
  "lon": "118.865949",
  "iata": "NKG",
  "name": "Nanjing Lukou International Airport"
 },
 {
  "cc": "CN",
  "lat": "31.1434",
  "lon": "121.805",
  "iata": "PVG",
  "name": "Shanghai Pudong International Airport"
 },
 {
  "cc": "CN",
  "lat": "31.198104",
  "lon": "121.33426",
  "iata": "SHA",
  "name": "Shanghai Hongqiao International Airport"
 },
 {
  "cc": "CN",
  "lat": "27.912201",
  "lon": "120.851997",
  "iata": "WNZ",
  "name": "Wenzhou Longwan International Airport"
 },
 {
  "cc": "CN",
  "lat": "29.712254",
  "lon": "106.651895",
  "iata": "CKG",
  "name": "Chongqing Jiangbei International Airport"
 },
 {
  "cc": "CN",
  "lat": "26.541466",
  "lon": "106.803331",
  "iata": "KWE",
  "name": "Guiyang Longdongbao International Airport"
 },
 {
  "cc": "CN",
  "lat": "30.31252",
  "lon": "104.441284",
  "iata": "TFU",
  "name": "Chengdu Tianfu International Airport"
 },
 {
  "cc": "CN",
  "lat": "30.558257",
  "lon": "103.945966",
  "iata": "CTU",
  "name": "Chengdu Shuangliu International Airport"
 },
 {
  "cc": "CN",
  "lat": "43.907100677490234",
  "lon": "87.47419738769531",
  "iata": "URC",
  "name": "\u00dcr\u00fcmqi Diwopu International Airport"
 },
 {
  "cc": "CN",
  "lat": "43.996201",
  "lon": "125.684998",
  "iata": "CGQ",
  "name": "Changchun Longjia International Airport"
 },
 {
  "cc": "CN",
  "lat": "45.623402",
  "lon": "126.25",
  "iata": "HRB",
  "name": "Harbin Taiping International Airport"
 },
 {
  "cc": "CN",
  "lat": "38.965698",
  "lon": "121.539001",
  "iata": "DLC",
  "name": "Dalian Zhoushuizi International Airport"
 },
 {
  "cc": "CN",
  "lat": "41.639801",
  "lon": "123.483002",
  "iata": "SHE",
  "name": "Shenyang Taoxian International Airport"
 }
]


payload = random.choice(airports)
print(json.dumps(payload, indent=4))


