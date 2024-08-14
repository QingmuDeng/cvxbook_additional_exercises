import numpy as np

s = np.array([0.41727435,0.83283272,0.82852249,0.77460460,0.54728298,0.52834997,
 0.50781749,0.52358051,0.68427120,0.97338698,0.95159444,0.94910509,
 0.99070007,0.94452588,0.85476515,0.92652186,0.90338521,0.26069605,
 0.79239624,0.82185329,0.55641790,0.67884699,0.72489186,0.88459221,
 0.99900000,0.99185291,0.99900000,0.98570079,0.77461056,0.84840970,
 0.78116716,0.90942174,0.74791375,0.91112252,0.99335189,0.99107686,
 0.61291945,0.81754282,0.95190907,0.71735702,0.72341395,0.81396815,
 0.99900000,0.95882616,0.97948261,0.97752644,0.99042217,0.99900000,
 0.83892736,0.92024356,0.80363354,0.69089739,0.87197904,0.90363402,
 0.95203164,0.69653977,0.90475626,0.94632555,0.94457059,0.95412865,
 0.97842397,0.86675007,0.77627892,0.88338240,0.73979147,0.80375385,
 0.89514267,0.93616569,0.93217107,0.89911988,0.76632646,0.79553101,
 0.93065526,0.50579279,0.99900000,0.91532222,0.60540231,0.80023285,
 0.99711374,0.99900000,0.99632245,0.96519885,0.66438153,0.92725029,
 0.95295875,0.95444100,0.95861434,0.86803473,0.95912909,0.91572408,
 0.99872638,0.96193863,0.90962143,0.95527465,0.93364735,0.52990254,
 0.99900000,0.89379231,0.97326619,0.95137698,0.94202612,0.94265618,
 0.94280026,0.70376670,0.93132554,0.71452008,0.58760702,0.45890861,
 0.69967445,0.47824488,0.68759627,0.92918310,0.97584513,0.84496995,
 0.95969121,0.94639009,0.57512411,0.99900000,0.81497858,0.55530173,
 0.95478604,0.97306580,0.96458797,0.95017093,0.60387749,0.99867848,
 0.99900000,0.98252884,0.99900000,0.96896792,0.93985495,0.65997117,
 0.98326123,0.99900000,0.95760213,0.94467311,0.94408447,0.62101459,
 0.99857873,0.95237431,0.91250043,0.86263207,0.86362709,0.86392524,
 0.87947650,0.87446237,0.64752052,0.97299459,0.99900000,0.78188701,
 0.89488275,0.92177038,0.95342643,0.89149653,0.86844125,0.79061882,
 0.69415871,0.86310889,0.86178553,0.86030463,0.80502750,0.86508038,
 0.68913109,0.85476838,0.98200773,0.92671679,0.99900000,0.99900000,
 0.98264413,0.93669917,0.94083218,0.75704508,0.94442769,0.85971405,
 0.33834957,0.91303483,0.93212002,0.99900000,0.99900000,0.91978950,
 0.00100000,0.94839977,0.94089741,0.93870500,0.92581007,0.81818466,
 0.80649927,0.84212116,0.17086370,0.28386216,0.90476402,0.94868939,
 0.76400167,0.59304177,0.81464582,0.95871339,0.89526352,0.77414113,
 0.59444822,0.80261997,0.91410397,0.67463091,0.62941712,0.81388363,
 0.87875227,0.75327774,0.40308206,0.90979450,0.92132957,0.94983439,
 0.66333041,0.90154736,0.85174801,0.29227719,0.31156622,0.99900000,
 0.99477254,0.97042750,0.98116537,0.99900000,0.98508540,0.98782485,
 0.98255515,0.97503793,0.97222953,0.97127169,0.95866628,0.86725036,
 0.83832388,0.95044013,0.95496083,0.66908285,0.74282528,0.99900000,
 0.98394129,0.98773718,0.94831042,0.95424321,0.96210528,0.95686993,
 0.88983817,0.94007966,0.72757785,0.72360906,0.84222778,0.81167139,
 0.74977227,0.80569630,0.40475941,0.92216517,0.64140664,0.99900000,
 0.95058443,0.88331458,0.54100085,0.98618611,0.75765455,0.61676129,
 0.88084426,0.94878979,0.95066784,0.89120447,0.65589482,0.78238436,
 0.61893230,0.95727660,0.99900000,0.96291331,0.92605363,0.93573922,
 0.82653261,0.58135745,0.99900000,0.93437644,0.97759509,0.95973044,
 0.93998813,0.92205401,0.96047828,0.90017411,0.75579520,0.19349075,
 0.19744898,0.35118493,0.76303475,0.91680341,0.92579708,0.72432897,
 0.84557525,0.94517565,0.99900000,0.99900000,0.97743545,0.94124332,
 0.98329815,0.95999250,0.85618703,0.98810667,0.87221754,0.94988691,
 0.91966453,0.93034925,0.89979732,0.78235920,0.72774039,0.78865627,
 0.96658786,0.92894601,0.53039974,0.50024889,0.52326862,0.81174464,
 0.62813420,0.57302826,0.59460948,0.74006045,0.91596047,0.74868030,
 0.61253185,0.58298871,0.51559720,0.61909635,0.78265706,0.53014432,
 0.71449990,0.99900000,0.95890512,0.95775557,0.85504375,0.89978603,
 0.80975570,0.74551913,0.62370719,0.48315622,0.59375192,0.40734225,
 0.60379956,0.97879528,0.87691492,0.96178428,0.75303463,0.62922947,
 0.73816000,0.73591092,0.37529220,0.66485868,0.33042740,0.43722392,
 0.54364068,0.34943153,0.72111032,0.96886017,0.97813841,0.97159584,
 0.94253087,0.92844736,0.87331660,0.92254354,0.89676903,0.87853633,
 0.91313132,0.91599350,0.83086323,0.89027106,0.86391412,0.87433533,
 0.68462949,0.78970569,0.74150031,0.82022922,0.80866718,0.78369916,
 0.78611162,0.83485396,0.81972957,0.88506920,0.89593935,0.85271012,
 0.88057923,0.84970031,0.74739331,0.73176115,0.85673147,0.85965451,
 0.86948094,0.85933085,0.86054717,0.85780940,0.84507735,0.83029638,
 0.82985915,0.82228755,0.82652846,0.81864908,0.80715032,0.77291249,
 0.80208682,0.83234549,0.81355440,0.76003748,0.80866546,0.58329535,
 0.54024979,0.76484985,0.52776763,0.78532782,0.86006159,0.83686077,
 0.73731874,0.83843260,0.84305660,0.85653782,0.88664532,0.85242477,
 0.82648694,0.84460216,0.78089764,0.80515739,0.81498285,0.79505298,
 0.79864407,0.80267098,0.72539526,0.54941837,0.81821360,0.80395066,
 0.76620850,0.76906545,0.64391536,0.76019701,0.68879936,0.78803978,
 0.74867787,0.74716711,0.60744093,0.77207741,0.74396023,0.76802258,
 0.79433749,0.53693109,0.39207583,0.77675794,0.82688359,0.78174524,
 0.76155173,0.70328302,0.53114910,0.25948002,0.70060557,0.68993405,
 0.75109545,0.75744037,0.74078991,0.62406805,0.70935176,0.69843789,
 0.69314843,0.69940090,0.71888023,0.64354644,0.67152542,0.66004226,
 0.61407800,0.70276078,0.62797206,0.70928939,0.68166834,0.68487743,
 0.33830414,0.35629658,0.62056712,0.42259764,0.62633228,0.61600534,
 0.55567105,0.88891946,0.90401798,0.92003128,0.92313621,0.94657435,
 0.31169347,0.29673167,0.97566266,0.88995244,0.64891621,0.62315913,
 0.75746775,0.30935702,0.75266250,0.86432010,0.97913733,0.95290092,
 0.90303326,0.91251713,0.84587899,0.75918470,0.85518726,0.85091951,
 0.86885324,0.87170876,0.75024657,0.85606502,0.84542729,0.73395075,
 0.73324265,0.87346377,0.85680960,0.68757221,0.51073772,0.91695066,
 0.91049400,0.87226165,0.91371941,0.91883812,0.67189970,0.73107980,
 0.82724255,0.94735770,0.91900214,0.96143807,0.94894808,0.94712128,
 0.90607552,0.91889574,0.72337705,0.66449680,0.86262122,0.72415395,
 0.30923837,0.34614994,0.76601728,0.75167630,0.82663144,0.43340667,
 0.61378088,0.98629254,0.98895970,0.97910753,0.84759952,0.25849243,
 0.24237294,0.46600449,0.98068441,0.93564989,0.90265433,0.91949256,
 0.91829900,0.85301526,0.49023320,0.15250674,0.87881950,0.46392174,
 0.64589018,0.94252317,0.50397910,0.89457990,0.65408481,0.84918565,
 0.49231284,0.42968285,0.61568243,0.11221520,0.82411281,0.90225791,
 0.89133091,0.90529417,0.91494169,0.60677726,0.92947747,0.21155801,
 0.79210146,0.12424609,0.73257650,0.93978396,0.93808880,0.93086700,
 0.97588323,0.97329948,0.95746267,0.95181747,0.87909037,0.02208140,
 0.86829920,0.28717460,0.50293098,0.28091224,0.18708898,0.48807082,
 0.70528088,0.76654874,0.23844500,0.29864752,0.99900000,0.92931847,
 0.84946576,0.93847833,0.75494541,0.11293621,0.29823587,0.50518424,
 0.60089952,0.48998647,0.98271196,0.99900000,0.97764543,0.83906441,
 0.53182131,0.16244981,0.99622600,0.98161835,0.99453748,0.96612132,
 0.70311503,0.60262738,0.99827716,0.94755808,0.94445299,0.94026704,
 0.81779158,0.93598901,0.83286809,0.90579020,0.83371500,0.82638775,
 0.86964160,0.80525089,0.79155855,0.88304425,0.60001297,0.30152238,
 0.71469238,0.97742598,0.93832814,0.72246582,0.70553482,0.86896902,
 0.93745766,0.94023842,0.92672164,0.94838244,0.93523595,0.94063105,
 0.57021788,0.87365527,0.90078063,0.77995616,0.85872139,0.77863436,
 0.78488141,0.96011104,0.92126986,0.93529031,0.84776317,0.96969885,
 0.96503007,0.89965927,0.81051585,0.84319137,0.87960949,0.94864005,
 0.92481856,0.91230542,0.89844944,0.74829619,0.80998882,0.85666667,
 0.77441713,0.92713121,0.98715659,0.97137076,0.95593664,0.93121198,
 0.90837965,0.91418383,0.48835275,0.38861799,0.70572700,0.97964710,
 0.60351453,0.33912847,0.98155112,0.75889577,0.54297939,0.88132786,
 0.80232068,0.69246903,0.57247988,0.98210502,0.99900000,0.53258102,
 0.98704407,0.94078546,0.94940161,0.80726455,0.39928546,0.74157689,
 0.70741773,0.99093300,0.38120821,0.47551273,0.24432116,0.49209429,
 0.85478823,0.31005723,0.73877375,0.57865978,0.30034620,0.28099755,
 0.57801413,0.81127023,0.36947717,0.75022596,0.99207289,0.99900000,
 0.99900000,0.99900000,0.97873200,0.39273616,0.95596814,0.92289612,
 0.90081462,0.86188268,0.62994761,0.86371144,0.78029329,0.92189619,
 0.93542500,0.96033922,0.94674915,0.86047419,0.74008850,0.04305558,
 0.76666536,0.84813054,0.88497376,0.82594848,0.83967362,0.85601865,
 0.04523121,0.73406172,0.83235242,0.83734176,0.79384852,0.81233047,
 0.78743837,0.73396807,0.74268604,0.80848222,0.79837217,0.75012474,
 0.83655017,0.83910973,0.63918009,0.80001374,0.34577611,0.60469230,
 0.75203595,0.81390782,0.59938421,0.43112308,0.78732072,0.68798135,
 0.75120589,0.51071383,0.78008341,0.80174547,0.81357948,0.81973155,
 0.65096332,0.76296546,0.78491164,0.80045438,0.73860202,0.71343118,
 0.83232914,0.77956946,0.63417293,0.84576922,0.90056124,0.87694908,
 0.84762626,0.80160208,0.80231202,0.87254832,0.68890264,0.60149092,
 0.52647037,0.84991776,0.85219180,0.86505985,0.85071260,0.85874372,
 0.77845456,0.83049169,0.72700512,0.47207037,0.23447915,0.84141213,
 0.79835972,0.82371631,0.71684550,0.78217017,0.81573937,0.75439843,
 0.75051467,0.72036716,0.63548525,0.66906217,0.59036410,0.32269982,
 0.61189997,0.53375390,0.52171599,0.50778418,0.91536310,0.91118240,
 0.90612599,0.01992980,0.87940154,0.90290500,0.88464783,0.87347132,
 0.75468094,0.74676893,0.76793089,0.68890191,0.86480251,0.88506563,
 0.85758592,0.86746329,0.68149671,0.78941450,0.81975541,0.81089105,
 0.81490440,0.80588163,0.81404162,0.84897805,0.82769461,0.78937125,
 0.79366792,0.43774314,0.64793121,0.82293853,0.83869929,0.82582862,
 0.85840755,0.84463716,0.83988592,0.83833951,0.19738135,0.41121286,
 0.43117745,0.51181349,0.00100000,0.00100000,0.00744657,0.90236252,
 0.66973475,0.00100000,0.00765890,0.77581973,0.76091494,0.00100000,
 0.00427117,0.48001337,0.80034568,0.79535721,0.00100000,0.00100000,
 0.00433846,0.85406196,0.00100000,0.00100000,0.00289347,0.77442543,
 0.00459214,0.79619349,0.78960211,0.73496981,0.84890121,0.72589013,
 0.79380898,0.66366791,0.77727551,0.75767197,0.70807349,0.77475654,
 0.90311852,0.86992361,0.86687389,0.78874155,0.79449559,0.76235030,
 0.82705256,0.83274236,0.82300913,0.79586373,0.80281125,0.76350153,
 0.80919953,0.75957529,0.77202816,0.45905862,0.83431027,0.82225206,
 0.68798095,0.78968493,0.66985807,0.63641351,0.73721106,0.75420074,
 0.74239614,0.72607698,0.59802756,0.58590024,0.74067798,0.44751033,
 0.67746096,0.65858223,0.52660305,0.62794510,0.17509573,0.52232370,
 0.80582418,0.83005722,0.83105196,0.82286601,0.79929906,0.78782281,
 0.70306288,0.01399316,0.80901379,0.49972898,0.85811631,0.82288342,
 0.82984877,0.83128760,0.83181523,0.58724501,0.81881502,0.79678109,
 0.84594087,0.80284518,0.58617405,0.83564335,0.82474008,0.80925383,
 0.82022032,0.83535310,0.84028808,0.79503904,0.83094119,0.84505831,
 0.85595402,0.35718144,0.82766837,0.74724076,0.89779036,0.71327339,
 0.88999604,0.88513127,0.90764554,0.88962049,0.93985246,0.93033212,
 0.94752274,0.79367706,0.92974890,0.89985366,0.88767884,0.76123784,
 0.70528004,0.91886189,0.91300532,0.19510669,0.63661438,0.94695636,
 0.94201187,0.93388483,0.39699625,0.69133240,0.77953302,0.19173549,
 0.45524059,0.67960521,0.46284498,0.84287082,0.95776755,0.78221698,
 0.96458735,0.81755222,0.89953072,0.61960474,0.48340683,0.21988000,
 0.84016132,0.86518185,0.86827233,0.95161984,0.95088634,0.93738128,
 0.90754298,0.85819341,0.74620586,0.64004541,0.61337310,0.69780127,
 0.43579230,0.51681640,0.79196548,0.59834823,0.72177499,0.85459354,
 0.87576549,0.91021050,0.87801630,0.90357164,0.91791967,0.46897672,
 0.90709872,0.94685856,0.93413231,0.83196504,0.93635807,0.86928662,
 0.95232199,0.87899315,0.94258841,0.92346801,0.88238297,0.72234692,
 0.88775919,0.86812588,0.68666416,0.63854284,0.30726407,0.96700701,
 0.94713220,0.94607631,0.90095842,0.92975285,0.82610028,0.91612030,
 0.89763912,0.30217748,0.56298952,0.68323695,0.95455733,0.78984364,
 0.97756417,0.91708856,0.68683073,0.40303381,0.33587387,0.32146389,
 0.45170176,0.35047264,0.32052788,0.79907414,0.85418737,0.69276669,
 0.76279567,0.54430408,0.42935979,0.75586756,0.97780017,0.98961462,
 0.93655289,0.89916172,0.52145366,0.63189264,0.87649495,0.96485218,
 0.96173792,0.93512450,0.95057942,0.92413635,0.94383933,0.81201680,
 0.88808167,0.72837528,0.53957554,0.72255398,0.89895566,0.68702154,
 0.67982194,0.71759906,0.45053174,0.75458716,0.85052166,0.81740754,
 0.80999330,0.83932890,0.70064603], dtype=np.float64)