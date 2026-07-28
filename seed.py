from app import create_app, db
from app.models import Lesson, Quiz, Question

app = create_app()

with app.app_context():
    # Clear existing demo data
    Question.query.delete()
    Quiz.query.delete()
    Lesson.query.delete()
    db.session.commit()

    # Create lessons
    lesson1 = Lesson(
        lesson_name='What is Forex?',
        content='FOREX, which stands for FOReign EXchange, is the global trading of currencies. More than $3.0 trillion in foreign exchange transactions take place each business day, and the volume is increasing steadily. Until the mid1990s the arena was the domain of large banks (the interbank market), governments, and corporations. Now it is possible for small speculators to trade online with any of a large number of retail FOREX broker-dealers using an online trading platform.\nIt is important to remember that a currency trade is between two currencies—a pair if one of them is the U.S. dollar (USD) and a cross\notherwise—and not a buy or sell of something such as a security (e.g., General Motors) or a commodity (e.g., gold) against the dollar.\nThe most popular currency pair is the EUR/USD—the Eurozone euroagainst the U.S. dollar. To be long this pair is to want the EUR to go up and\nthe USD to go down. To be short this pair is to want the USD to go up and\nthe EUR to go down.\nThere is no central clearinghouse for currency trading as there is for\nstocks or commodity futures. It is the closest thing there is to a pure laissezfaire market. That cuts both ways: The opportunities are enormous but it\nis a largely unregulated and often cutthroat enterprise.\nIn the United States, retail FOREX is partially regulated by the Commodity Futures Trading Commission (CFTC) and the National Futures\nAssociation (NFA). But, with no central clearinghouse, regulation is by\ndefinition less robust and effective than in stocks or commodity futures.\nRegulation is largely limited to seeing that retail brokers meet certain capital requirements and follow good-practice guidelines. Caveat emptor\r\nis the watchword in FOREX.\r\n\r\nWHY TRADE FOREX?\r\nDespite the risks, the retail market is growing by leaps and bounds. Obviously, many traders have concluded that the opportunities outweigh those\r\nrisks. Here is a short list of why people are attracted to currency trading.\r\nNo commissions. There are typically no clearing fees, no exchange\r\nfees, no government fees, and no commissions. FOREX works off\r\na bid/ask spread and the costs are contained therein. Some brokers\r\nwho use the electronic communications network (ECN) transaction model, however, also may charge a small lot fee.\r\nHigh liquidity. With an average of over $3 trillion in transactions\r\ndaily, it is easy to execute even very large orders in foreign exchange. Online brokers most often offer instantaneous fills on retail orders.\r\nNo fixed lot size. The standard lot size in retail FOREX is 100,000\r\nunits. Most brokers offer mini-lots of 10,000, and some let you\r\ntrade as few as 100 units! The variable lot size can be an excellent money management tool for the trader. It also allows the new\r\ntrader to gradually increase trade size as his or her knowledge and\r\nprofits rise.\r\nA 24-hour market. There is no opening bell in FOREX! You may trade\r\nfrom late Sunday afternoon (U.S. time) to late Friday evening. You\r\nmay come and go as you like, and trade for as long a time or as\r\nshort a time as you wish.\r\nOnline access. All retail FOREX is conducted online, via the Internet.\r\nYou will trade from a broker’s trading platform, which typically includes not only real-time prices and the ability to place buy and\r\nsell orders but also a variety of trading tools such as charts and\r\nindicators. Most brokers allow clients to call in orders by phone if\r\nthe need arises.\r\nLow margin, high leverage. Perhaps the most attractive element to\r\nFOREX trading is the ability to trade leverage ratios of from 10:1 up\r\nto 400:1! This means that you may control 100,000 USD with from\r\n$10,000 to as little as $250. With high leverage, a very small move\r\nmay result in a 100 percent profit—or loss. Gradually increasing\r\nleverage can also be an effective money management tool.\r\nVolatility. The FOREX markets can move quickly and sharply; profits\r\ncan be large if you are correct in your price forecast.\r\nVariety. There are more than 30 currency pairs and crosses traded,\r\nalthough most of the volume is concentrated in about half of those.\r\nMany traders claim individual pairs and crosses have personalities\r\nthat help them make forecasts. There is enough variety to keep\r\nopportunities plentiful, but not so much as to be bewildering and\r\nconfusing.\r\nNot related to the stock market. Currencies most often move independently of the stock market, although there has been a close\r\ncorrelation during the 2008 financial crisis as equities are used as\r\na measure of risk aversion. From an investment perspective it is\r\nsaid that currency prices are noncorrelated with stock prices. For\r\nthis reason FOREX may be an attractive hedge to a larger stock\r\nmarket account.\r\nLimited regulation. Because FOREX is a global interbank enterprise,\r\nregulation is necessarily limited. This, of course, can cut both\r\nways, as mentioned earlier.\r\nNo insider trading. It is difficult to get useful inside information on\r\ncurrencies. Even if you did know in advance a key government\r\nstatistic, the markets are so unpredictable that it is not often easy\r\nto foretell which way the market will go after a news release.\r\n\r\nCountries with popularly traded currencies include:\r\n\x01 United States\r\n\x01 European Union\r\n\x01 Switzerland\r\n\x01 Great Britain\r\n\x01 Japan\r\n\x01 Canada\r\n\x01 Australia\r\n\x01 New Zealand',
        video_url=None,
        course_id=1
    )

    lesson2 = Lesson(
        lesson_name='Forex Terms and Calculations',
        content='Here are the most important FOREX terms. To a large extent, learning the\nsyntax or lingo of FOREX is learning FOREX itself.\nAsk price. The price at which the market is prepared to sell a specific currency in a foreign exchange contract or cross currency\ncontract. At this price, the trader can buy the base currency. In the quotation, the ask price is shown on the right-hand side. For\r\nexample, in the quote USD/CHF 1.4527/32, the ask price is 1.4532,\r\nmeaning you can buy one U.S. dollar for 1.4532 Swiss francs.\r\nBase currency. The first currency in a currency pair (for example,\r\nUSD is the base currency in the currency pair USD/CHF). The rate\r\nshows how much one unit of the base currency is worth as measured against the second currency. For example, if the USD/CHF\r\nrate equals 1.6215, then one USD is worth CHF 1.6215. In the foreign exchange markets, the U.S. dollar is normally considered the\r\nbase currency for quotes, meaning that quotes are expressed as a\r\nunit of $1 U.S. per the other currency quoted in the pair. The primary exceptions to this rule are the British pound, the Eurozone\r\neuro, and the Australian and New Zealand dollars.\r\nBid price. The price at which the market is prepared to buy a specific currency in a foreign exchange contract or cross currency\r\ncontract. At this price, the trader can sell the base currency. It is\r\nshown on the left-hand side of the quotation. For example, in the\r\nquote USD/CHF 1.4527/32, the bid price is 1.4527, meaning you can\r\nsell one U.S. dollar for 1.4527 Swiss francs.\r\nBid/ask spread. The difference between the bid and ask (offer) price.\r\nBig figure quote. Dealer expression referring to the first few digits of\r\nan exchange rate. These digits are often omitted in dealer quotes.\r\nFor example, a USD/JPY rate might be 117.30/117.35, but would be\r\nquoted verbally without the first three digits, that is, as “30/35.”\r\nClosed position. A foreign currency position that no longer exists.\r\nThe process to close a position is to sell or buy a certain amount\r\nof currency to offset an equal amount of the open position. This\r\nwill square the position.\r\nCorrelation to the stock market. At the time of this writing currencies are moving in close correlation with the stock market. This is\r\nnot always the case, however. Professional traders do watch for\r\nchanges in correlation as an aid to decision making in placing FX\r\norders. The switch between being correlated and non-correlated\r\nhappens slowly over longer periods of time.\r\nCounter currency. The second listed currency in a currency pair.\r\nCross currency pair. A foreign exchange transaction in which one\r\nforeign currency is traded against a second foreign currency. For\r\nexample, EUR/GBP is the euro versus the British pound.\r\nCurrency pair. The two currencies that make up a foreign exchange\r\nrate, for example, EUR/USD.\r\nElectronic communications network (ECN). A system wherein\r\norders to buy and sell are matched through a network of banks and/or dealers. See also market maker; no dealing desk (NDD)\r\nbroker.\r\nFlat/square. Refers to a trader on the sidelines with no position.\r\nForeign exchange (FOREX, FX). The simultaneous buying of one\r\ncurrency and selling of another.\r\nFOREX (FX). Foreign exchange.\r\nGoing long. The purchase of a stock, commodity, or currency for investment or speculation.\r\nGoing short. The selling of a currency or instrument not owned by the\r\nseller.\r\nLeverage. The ratio of the amount used in a transaction to the required\r\nsecurity deposit, otherwise known as margin. Leverage is typically\r\nquoted as a ratio. For example, 100:1 means one dollar controls\r\none hundred dollars of a currency. A 1 percent move of the currency is equal to a 100 percent gain or loss of margin.\r\nLong position. A position that appreciates in value if market prices\r\nincrease. When the base currency in the currency pair is bought,\r\nthe position is said to be long.\r\nLot. A unit used to measure the amount of the deal. The value of the\r\ndeal always corresponds to an integer number of lots.\r\nMajor currency. Any of the following: Eurozone euro, British pound\r\nsterling, Australian dollar, New Zealand dollar, U.S. dollar, Canadian dollar, Swiss franc, Japanese yen. See also minor currency.\r\nMargin. The required equity that an investor must deposit to collateralize a position.\r\nMarket maker. A dealer who regularly quotes both bid and ask prices\r\nand is ready to make a two-sided market for any financial instrument. Most retail FOREX dealers are market makers. A market\r\nmaker is said to have a dealing desk and is the effective counterparty to your trade.\r\nMinor currency. Any of the currencies between a major currency and\r\nan exotic. The South African rand and Swedish krona are minor\r\ncurrencies.\r\nMundo. A synthetic global currency devised by James L. Bickford, calculated as the average of multiple ISO currency pairs. See Michael\r\nArcher and James Bickford, Forex Chartist Companion (John\r\nWiley & Sons, 2006).\r\nNo dealing desk (NDD) broker. Provides a platform to which liquidity providers such as banks can offer prices. Incoming orders are routed to the best available bid or offer. See also market maker;\r\nelectronic communications network (ECN).\r\nShort position. A position that appreciates in value if the market price\r\ndecreases. When the base currency in the pair is sold, the position\r\nis said to be short.\r\nTrading platform. The online set of tools used to trade FOREX. Trading platforms provide real-time prices of currencies, order entry\r\nmechanisms, accounting logs, and a variety of trading tools such\r\nas calculators, charts, and indicators.\r\nThe Glossary offers a comprehensive FOREX lexicon.\r\nFOREX CALCULATIONS\r\nThe calculations in FOREX can be confusing, although they are not inherently difficult. Study will get you only so far; practice is the key. Use an online FOREX calculator to see how the various calculations work, then practice with a demo account from one of the brokers we highlight in Chapter\r\n7. More on calculations used in FOREX is provided in Chapter 2 on money\r\nmanagement.\r\nYou’ll eventually need to be able to make these calculations instantaneously; the FOREX markets move quickly, real-time, and you’ll need to\r\nconcentrate on trading, not calculations. But don’t worry if they don’t come\r\nto you right away.\r\nMost broker trading platforms have FOREX calculators you can use to\r\nbecome familiar with how the various values and units interact.\r\nRemember that a currency transaction is between two currencies, not\r\na single currency and a product as is true in stocks and commodity futures.\r\nYou may either buy or sell a currency, profiting if it goes up or down. If\r\nyou buy a currency, you are said to be long and an offsetting transaction\r\nis to sell. If you sell a currency, you are said to be short and an offsetting\r\ntransaction is to buy.\r\nEUR/USD is the symbol for the euro-to-U.S. dollar currency pair. If you\r\nbuy, you are going long the front or base currency and effectively short the\r\nback or counter currency. If you sell, you are going short the base currency\r\nand effectively long the counter currency.\r\nThe basic calculations you will want to learn are the following:\r\nLeverage and Margin Percent\r\nLeverage = 100 ÷ Margin Percent\r\nMargin Percent = 100 ÷ Leverage\r\nLeverage is typically quoted as a ratio of X:1, where 1 is the margin for\r\nthe position and X is the value of the position. For example, 100:1 means\r\nyou control 100 times the margin amount. Typically anything under 50:1\r\nis considered low leverage, whereas over 100:1 is very high. New traders\r\nshould begin with low leverage (e.g., 10:1) and increase by 10:1 units as\r\ntheir confidence increases and until they maximize their money management parameters.\r\nPips\r\nA pip is typically the smallest increment that any currency pair can move in\r\neither direction, up or down. In FOREX, profits and losses are calculated in\r\nterms of pips first, dollars second. The pip is very much the basic FOREX\r\nvalue. Some brokers now offer fractional pips on the more popular pairs.\r\nThe pip is typically $10 on a 100,000 currency lot, $1 on a 10,000 lot, and\r\n$25 on a 250,000 “bank” lot.\r\nProfit and Loss\r\nVery basically, profit or loss is price change, which in turn is exit price\r\nminus entry price. If the value is positive, you made a profit; if it is negative,\r\nyou lost.\r\nProfit in Pips = Price Change × Pips\r\nProfit in USD = Price Change × Units Traded\r\nTrading Units\r\nYou will always want to know how many units of a pair you can\r\nbuy or sell. Again, almost all broker-dealer trading platforms offer this\r\ninformation—but you should know how to calculate it on your own, also.\r\nUnits Available = 100 × Margin Available × Rate ÷ Current Price\r\n× Margin Percent\r\nIf the USD is the base currency:\r\nUnits Available = 100 × Margin Available ÷ Margin Percent\r\nStandard trading units are 10,000, 100,000, and 1,000,000.',
        video_url=None,
        course_id=1
    )

    lesson3 = Lesson(
        lesson_name='CFTC Warning',
        content='Money management includes trading wisely and husbanding your\ntrading resources. FOREX speculation involves significant risk taking. Never risk what you cannot afford to lose. You cannot trade\nwithout trading capital, so capital preservation is critical. One key to holding on to your capital is the appropriate use of leverage. The required\nCommodity Futures Trading Commission (CFTC) warning statement on\nthe Global-View web site contains a lot of wisdom for traders of any instrument. This chapter also discusses appropriate leverage strategies and\nprovides a list of trading rules.\nComing into the trading game, it is important to realize that all traders\nhave many losing trades. Be aware of this before starting. Stop loss orders\nare often not used by novice traders; use them, as they are critical to your\ntrading survival.\nIt is not our intention in this chapter to be negative, but the majority\nof the items covered here are “don’ts” as opposed to “do’s” if only because\nnew traders seem to major in “don’t.” The following are some important\nthoughts from an experienced European trader.\nTrading is not mainly about making money but more about CAPITAL PRESERVATION. Think about it. NO CAPITAL, NO TRADING!\nEach time you enter a trade you should think “How much I am\nready to lose!” and not “How much I am HOPING to make!”\nTrading is simple, but it is not easy!\r\n\r\nCFTC WARNING\r\nMany of us see a warning label or disclosure statement and just gloss over\r\nit. The required CFTC warning statement about FOREX trading on margin\r\ncontains useful information that is worth taking a few minutes to read and\r\nthink about. Many of the topics covered in this chapter relate to the items\r\nmentioned in this required statement:\r\nTrading foreign exchange on margin carries a high level of risk, and\r\nmay not be suitable for all investors. The high degree of leverage can\r\nwork against you as well as for you. Before deciding to invest in\r\nforeign exchange you should carefully consider your investment objectives, level of experience, and risk appetite. The possibility exists\r\nthat you could sustain a loss of some or all of your initial investment\r\nand therefore you should not invest money that you cannot afford to\r\nlose. You should be aware of all the risks associated with foreign\r\nexchange trading, and seek advice from an independent financial\r\nadvisor if you have any doubts.',
        video_url=None,
        course_id=2
    )

    lesson4 = Lesson(
        lesson_name='Key to success as a trader: Preserve your capital',
        content='Capital preservation is the key to trading success at all levels, from the\nsmall individual trader to the sophisticated large hedge fund manager, and\nit must be goal number one. Without sufficient capital, a player cannot participate in the markets. In the warning statement, the CFTC states that “The\nhigh degree of leverage can work against you as well as for you.”\nA common error of new traders is overleveraging their trading capital.\nLater in the chapter we discuss how to calculate your leverage and recommend a commonsense approach to how much of your trading capital to put\nat risk on any given trade.\nTHE INSIDE SCOOP (JAY MEISLER)\nTypically, it seems that traders don’t come to us until they are about to blow\ntheir accounts. The source of the problem is usually a lack of discipline that\nturned a manageable loss into a crisis situation. I remember one instance where\na trader who used to be in regular contact disappeared from sight. I sensed\nsomething was amiss when attempts to contact him went unanswered. He was\nembarrassed to tell what happened as he saw the capital in his account dwindle with each passing day. By the time he contacted me, he had already blown his\r\naccount.\r\nThe problem started with a short-term trade taken following the release of\r\nsome economic news. The market moved against him and he never recovered.\r\nAn attempt to earn 20 pips wound up losing over 700 pips as the market trended\r\nthe other way. Doubled-up trades failed. Hope replaced solid analysis. Prudent\r\nmoney management and discipline were tossed aside. Proper risk/reward measurement had long since passed.\r\nIn situations like this, when a trader asks for advice on a losing position\r\n(I would hope before it reaches a critical point), I ask one question: “If you were to\r\nstart with a clean slate right now, would you take this position?” If the answer is\r\nno, then the trader has answered his own question and should exit the position.\r\nIf asked for my advice before a trade is placed, I ask: “What is your profit target\r\nand what is your stop?” This is because a trader needs to establish a risk/reward\r\nobjective on a trade before trading. Also, one must have a stop in place in order\r\nto live to trade another day if the trade does not work out as planned.',
        video_url=None,
        course_id=2
    )

    lesson5 = Lesson(
        lesson_name='What is leverage?',
        content='Since outright percentage price moves in currencies often tend to be significantly smaller than those on equities or on some commodities, a 10 to 20\npercent annual price swing in the value of one currency versus another is\nconsidered to be substantial. FOREX trading in the commodity markets or\nwith an online broker is done on a leveraged basis to amplify (or leverage)\npotential trading gains or losses. In other words, a small margin deposit\ncan buy control over a much larger position. A margin deposit is best described as good-faith or earnest money. It in no way limits the potential\nloss on a position. The buyer or seller of a position in the FOREX market\nis liable for any losses on the full position, and of course would benefit\nfrom any gains. For example, a USD500 margin at some firms might control\na EUR100,000 position (equal to $148,000 at an exchange rate of EUR/USD\n1.4800).\nLeverage is often expressed as a ratio:\nLeverage = Trading Position/Required Margin\nThus in our example:\nEUR100,000 @ 1.4800 = USD148,000\r\nThe typical required margin is USD500:\r\nUSD148,000/USD500 = 296\r\nThe leverage is:\r\n296:1\r\nOn the regulated commodity exchanges, the comparable FOREX leverage might be about 65:1. Some FOREX brokers advertise leverage as high\r\nas 400:1',
        video_url=None,
        course_id=2
    )

    lesson6 = Lesson(
        lesson_name='What is technical analysis?',
        content='T here are two methods for analyzing markets in general and FOREX\nmarkets in particular: technical analysis and fundamental analysis.\nMany traders use both, but technical analysis predominates today.\nThere are still many fundamental-based professional traders, but almost\nall retail and amateur traders use technical analysis exclusively. Most large\nFOREX funds are driven by computerized trading systems in a field referred to as quantitative analysis, which often access both technical and\nfundamental data. This chapter looks at some of the more popular technical trading methods—and a few lesser-known methods.\nThe debate over which is better—technical analysis or fundamental\nanalysis—has raged for decades. Each side has its strengths and weaknesses.\nFundamental analysis attempts to forecast prices by reference to the\neconomic events underlying the currency for a given country—or the two\ncurrencies in a traded pair. These events are typically offered as quantitative statistics such as balance of payments, monetary growth, and the\nlike. There is no doubt that ultimately long-term trends are fundamentally\ndriven. But as Lord Keynes said, “In the long run we are all dead.” When\nyou are dealing with leverage factors of 100:1 and higher, how important is\nthe long run? Can you sit out a $5,000 loss on a small trade to eventually\nmake $100?\r\nOpinions from an Australian trader on the inability of markets to price\r\nin future events:\r\nThe markets are incapable of actually seeing beyond the data which\r\nis presented to them. Risks are not something to be factored or priced\r\nin but are unforeseen changes in the landscape that will be revealed\r\nat some future date.\r\nThere are two other issues the technician will proffer in the argument\r\nagainst fundamentals:\r\n1. Some of the fundamental factors are not quantifiable.\r\n2. The relationships between the factors are constantly changing, and in\r\ncomplex, nonlinear ways. The weights of each factor—and there are\r\nperhaps hundreds of them—fluctuate enormously and are probably unpredictable.\r\nBut even the technician will acknowledge that one should trade with\r\nthe major trend—a trend certainly determined by fundamentals. “The trend\r\nis your friend” is an old and remarkably helpful market adage. Don’t fight\r\nthe trend; trade with it.\r\nFrom a London based trader:\r\nIf a true fundamental analysis was to be applied to the current market then we would see a completely different picture.\r\nWhat is a “true fundamental” analysis?\r\nFor now we have a predominance of technical over fundamental\r\ninfluence in the market. One could project many inferences on the\r\nmarket for this reason.\r\nIt sounds like you are saying that technicals dominate when no\r\ntrends can be found, but technicals include trends so I’m not sure\r\nwhat this means at all besides the fact that there is no agreed-upon\r\nsingle technical analysis nor any agreed upon fundamental analysis\r\ntechnique. They just look at different sources of information... .\r\nChapter 3 was written by Mike Archer. Author Bland (a fundamentalist) and Meisler wrote Chapter 4. Readers can see for themselves\r\nthe point-counterpoint between the two schools of thought.\r\n\r\nWHAT IS TECHNICAL ANALYSIS?\r\nThe technician begins with the axiom that everything is in the price,\r\nready and waiting for analysis. The methods by which this data is\r\nmanipulated—tortured if you will—are enormously varied and often quite\r\ncreative and complex.\r\nPrices are the primary data available to FOREX traders. Because there\r\nis no central clearinghouse, volume (the number of trades executed) and\r\nopen interest (the number of open or outstanding trades) available to commodity futures traders are nonexistent. Efforts have been and are being\r\nmade to synthesize those factors for currency pairs to give FOREX traders\r\nadditional data with which to work.\r\nA fundamentalist might argue there is nothing in past prices that would\r\nforetell future prices. The data is but a dead record of the past. A moving\r\naverage tells everything about the past but nothing about the future. The\r\ntechnician counters that every buyer in the market must sell to exit and\r\nevery seller in the market must buy to exit. That information, they hope, is\r\nsomehow coded in the record of past prices. Author Archer is developing\r\na system, the Trend Machine, that uses cellular automata in an attempt to\r\ndecode past prices and reconstitute them into forecasts.\r\nEconometric modeling is something of a hybrid approach. The statistical information of fundamentals is manipulated mathematically to create\r\na pricing model. Since, as noted earlier, the relationships and weights of\r\nthese factors are nonlinear, the only model that might work is one using\r\nnonlinear mathematics or structures such as chaos, catastrophe, or cellular automata.\r\nMost broker-dealer trading platforms have a large palette of technical\r\ntools for the trader—charts and indicators. A number of third-party vendors offer more robust technical analysis packages. See Chapter 13 of Getting Started in Currency Trading, Second Edition (John Wiley & Sons,\r\n2008) for some current offerings.\r\nIf you do use a third-party analysis suite, remember that if it does not\r\nintegrate with your broker’s trading platform (many do), the prices and\r\nsignals off your technical tools may differ slightly from those on the trading\r\nplatform.',
        video_url=None,
        course_id=3
    )

    lesson7 = Lesson(
        lesson_name='Technical analysis landscape',
        content='The primary division in technical analysis is between chart reading and indicators. A chart is essentially a picture, or graphic record, of prices. Some\n36 THE BASICS OF FOREX\ncharting methods are very old; candlestick charts date to the sixteenth\ncentury.\nIndicators generally fall into two classifications: trend following or\ntrading. Indicators became popular in the 1970s and there are hundreds\nof them. Indicators in turn are generally of two flavors; they are designed\nfor either sideways markets or trending markets.\nA secondary division might be found between methods and systems.\nA method is typically a combination of technical analysis tools, used together but not fully automated. A system is a method that has been fully\nautomated and runs without outside interpretation or judgment. Most large\nhedge funds now use systems, and the entire field is referred to as quantitative analysis and algorithmic trading.\nMost technical traders use both charts and indicators. But try to keep\nyour toolbox simple and be wary of overlap where two or more tools\nmeasure the same thing—for example, two indicators that both pertain\nto sideways markets. Systems and methods are essentially combinations\nof tools used by a trader. A system is generally an automated, nondiscretionary approach, whereas a method still requires the trader to make the\nfinal decision.\r\nCharts\r\nBar Charts Bar charts (Figure 3.1) are not the oldest form of charting,\r\nbut they are the most commonly used. All broker-dealers offer bar charts\r\nas part of their charting packages.\r\nA bar represents some fixed, closed-end time frame. In stocks and commodity futures, it is typically one week or one day. In FOREX, bar charts\r\nmay range from one minute to one month. The most popular for trading\r\ntend to be five-minute to one-hour charts. Each bar is a vertical line representing the high and low plus short horizontal lines indicating the close (to\r\nthe right of the bar) and oftentimes the open (to the left of the bar) for that\r\ntime frame.\r\nClassical bar chart formations with interesting names are still watched\r\nfor by traders. A double bottom appears in Figure 3.2.\r\nUnfortunately, the more popular a chart formation or indicator\r\nbecomes, the less often it is likely to appear. The market discounts\r\ninformation. For example, consider the head and shoulders formation, diagrammed in Figure 3.3. As traders begin to see it form on a price chart, they\r\noften anticipate the right shoulder and begin selling. The result will be that\r\nthe shoulder never actually is built and the formation fails to materialize railroad stocks. Although now out of favor, they are easy to use and interpret. Unfortunately, very few broker-dealers offer point and figure charts\r\n(they are available from third-party vendors, however).\r\nWhereas bar charts are time frame sensitive, point and figure charts\r\nare only price sensitive; you cannot tell when a price occurred on a point\r\nand figure chart. Uptrends are shown as a vertical column of Xs and downtrends as a vertical column of Os. The trader must decide two parameters:\r\nthe value of each X and O box and how many boxes are required to cause a\r\nreversal (i.e., begin a new column in the opposite direction). Three-box reversals are the most common, but one-box and five-box reversals are also\r\nused by traders.\r\nPoint and figure formations may be more reliable than bar chart formations, if only because point and figure charts are less in use by today’s\r\ntraders.\r\nCandlestick Charts Candlestick charts (Figure 3.5) compete with bar\r\ncharts for popularity. They date from the Orient in the sixteenth century. Several books offer instruction on how to interpret them. Most\r\nbroker-dealers offer candlestick charts on their trading platforms because\r\nof their popularity and the wealth of methods for their interpretation.\r\nSwing Charts Swing charts have fallen out of favor. They are very similar to point and figure charts, but use vertical lines instead of Xs and Os.\r\nThere are four primary types of swings, shown in Figure 3.6. These\r\nswings can also be seen on bar charts. They are bull, bear, inside, and outside (referenced to the previous swing). A bull swing has a higher high and\r\na higher low. A bear swing has a lower high and a lower low. An inside\r\nswing has a lower high and a higher low. An outside swing has a higher\r\nhigh and a lower low.\r\nWhile all broker-dealer platforms offer integrated charting tools, there\r\nare also many third-party vendors with excellent charts. We like FXtrek\r\n(www.intellicharts.com) for quality, cost-effective charts, but there are\r\nseveral others to consider.',
        video_url=None,
        course_id=3
    )

    lesson8 = Lesson(
        lesson_name='Wha is fundamental analysis?',
        content='T he age-old debate among traders about which is the better way to\nmake decisions—technicals or fundamentals—misses the point. The\ntwo are not mutually exclusive; they are complementary. Activity in\nthe interbank FOREX market is far larger than the retail trading platforms\nand commodity markets. The relative volume of retail trade is insignificant\ncompared to institutional activity. Many institutional dealers rely heavily\non the fundamentals, so it behooves the retail trader to have a passing\nknowledge of the fundamentals, if for no other reason than to understand\nwhat the big players are up to. This chapter aims to provide an insight into\nwhat factors fundamental traders consider when they make their trading\ndecisions.\r\n\r\nWHAT IS FUNDAMENTAL ANALYSIS?\r\nThe fundamental trader seeks to figure out the reasons behind buying or\r\nselling currencies in the FOREX markets in order to predict how those\r\nmaking such transactions will behave in the future. The technical trader\r\nsimply accepts the fact that these transactions are taking place and looks\r\nfor familiar price patterns to repeat. This chapter takes a quick look at\r\nsome of the principal fundamental influences on the markets. Because\r\nknowledge of the fundamentals usually requires both academic preparation and considerable market experience, they are often used more frequently by traders who have a professional background. If you approach\r\nboth analysis tools with an open mind, you might find that some of the elements of a fundamental approach might prove to be useful along with\r\ntechnicals. Figure out what works for you.\r\nALL PRICE MOVES ARE NOT\r\nCREATED EQUAL\r\nMany assert that the fundamentals are already priced in the markets.\r\nDecades of trading experience suggest that this theory is utter nonsense.\r\nTake a look at how the direction of the markets can be abruptly reversed\r\nby a central bank decision or an economic release. As for the difference between fundamental and technical analysis, the two methods approach the\r\nmarkets from different directions. Technical traders look for future guidance from past and present price patterns, while fundamental analysts like\r\nto dig in and try to figure out what is behind the price patterns that the\r\ntechnical traders are readily accepting.\r\nA basic flaw with pure fundamental trading is that it is often impossible\r\nbefore the fact to identify which fundamental factors will be dominating\r\ntrade, because those factors tend to change quickly. A key flaw in pure\r\ntechnical trading is that it can lack the depth that comes from fundamental\r\nanalysis. In other words, not all price moves are created equal. Here is how\r\na bank dealer from the southern tier of Europe approaches the FOREX\r\nmarkets:\r\nToday’s data really puts into context those three basics that move\r\nfx rates: relative growth differentials, yield differentials, and other\r\nstuff. In a rising growth/low volatility environment, yield differentials matter more. In the current falling growth and risk aversion environment, yield differentials matter little. It’s primarily\r\nabout future relative growth expectations, and how some economies\r\nare soon to be perceived as falling more behind the curve than\r\nothers.\r\nAn approach that might be considered is to use whatever technical\r\napproach works for you and supplement that strategy with an awareness\r\nof what is happening fundamentally.',
        video_url=None,
        course_id=4
    )

    lesson9 = Lesson(
        lesson_name='Interest Rates',
        content='Think of foreign exchange as just another commodity. Money tends to flow\nto where it earns the most and moves away from where it earns the least.\nAn investment in a currency has “costs.” The first and most volatile cost\ncan be its exchange value against the home currency of the investor and\nthe second is the ongoing interest rate cost of financing the position in\nthat currency. Below we will discuss how interest rate differentials impact\nthe cost of trading (rollover) and how rate movements have an impact on\nmacro moves in the foreign exchange markets.\nRollover Costs\nAlthough it is not transparent at all times to retail traders, FOREX transactions all have baked in a cost based on interest rate differentials. Sometimes this cost can be negative so that a position earns something, but there\nis always a daily net interest rate gain or loss cranked into the rollover or\nforward rates. In other words, you earn on the rollover when holding a\nhigher-yielding currency, and the opposite is true when you hold a loweryielding currency.\r\nThus a JPY purchase for USD has to be financed at some level by borrowing USD to hold on to a JPY bank deposit. If it costs 5.50 percent per\r\nannum to borrow USD for one day and a JPY deposit earns 0.50 percent for\r\none day, the cost of running a long JPY position against the USD would be\r\n5.00 percent per annum. A transaction in the opposite direction would earn\r\n5.00 percent per annum. This is where the rollover costs or credits come\r\nfrom. In this example, the charge or credit for one day would be minimal,\r\nbut for long-term capital flows, the cost over the course of a year could\r\nbecome considerable.\r\nThere are cases where interest rate differentials have been substantial\r\nand have remained that way for considerable periods of time. Since the\r\nearly 1990s, the Bank of Japan has kept interest rates low in an effort to lift\r\nits economy out of deflation (declining prices). Thus the cost of borrowing\r\nJPY has been close to zero for years. Hedge funds and others (Japanese\r\ninvestors) have been borrowing cheap JPY and investing those funds in\r\nhigh-yielding currencies, such as the AUD. This is often referred to as a\r\ncarry trade. Those with a longer-term perspective currently can borrow\r\nJPY, invest in AUD, and earn a 6.10 percent interest rate spread for a year.\r\nOf course the trade involves exchange rate risk, but that’s the risk that\r\nmany investors both inside and outside of Japan have been taking for a\r\ngood while. In this example, those borrowing JPY (at a cheap interest rate)\r\nwill buy AUD, and then place the proceeds of the transaction into an AUD\r\nbank deposit. This transaction results in JPY selling and AUD buying that\r\nfundamental traders will try to anticipate.\r\nJPY borrowers (hedge funds and others) have also borrowed JPY to\r\ngenerate the cash to pay for investments in equities, oil, gold, NZD, and\r\nother vehicles. These trades have generated capital flows out of Japan,\r\nwhich kept the JPY weak for years as these investments were paid for by\r\nnew JPY liabilities.\r\nNote that these strategies are not a one-way street. The financial crisis in the second half of 2008 has led to massive unwinding of these “carry\r\ntrade” positions, boosting both the yen and dollar versus all currencies, as\r\nglobal markets were forced to de-leverage. This created heightened volatility and risk aversion, which both rose to historically high levels. While technicians might say it was all in the charts, these extraordinary moves in the\r\nFOREX market were led by fundamental factors. Differentials in short- and\r\nlong-term interest rates often establish the underlying flow (or currents) in\r\nthe markets, as in the case of a river. For this reason a lot of time is spent in the major institutional trading rooms trying to forecast future interest\r\nrates. It is the role of a country’s central bank to support its economy. Central banks, such as the U.S. Federal Reserve (the Fed), have a dual mandate to contain inflation and support economic growth, while other banks,\r\nsuch as the European Central Bank (ECB), have a single mandate to ensure price stability. In recent years, more and more of the central banks\r\nhave started to target a specific inflation level. The theory is that if inflation\r\nis contained, economic growth will take care of itself. Global-View.com\r\nmakes available in its public pages free central bank analysis accompanied\r\nby relevant charts that are updated daily.\r\nOne trading strategy that might be considered is to find whatever technical approach works best for you and to supplement those signals with an\r\nawareness of what is happening fundamentally',
        video_url=None,
        course_id=4
    )

    lesson10 = Lesson(
        lesson_name='Caveat Emptor (Let the Buyer Beware)',
        content='Trading the news—trading into or right after a news release—can be\ncomplex and risky. Nevertheless, retail FOREX traders have a love\naffair with trading after economic data or other news is released. Two\nreasons for the love affair are there is something tangible to trade off and\nthere is generally volatility right after the news is reported. This volatility\ncreates opportunities for quick profits but also poses risks to those who do\nnot understand the mechanics of the interbank market, especially during\nthese periods of volatile price action.\nThe purpose of the following example is not to defend brokers but to\neducate the retail trader as to the realities of trading the news.\r\n\r\nCAVEAT EMPTOR (LET THE\r\nBUYER BEWARE)\r\nThe pros know what to expect following a major economic or other news\r\nreport. They expect liquidity to thin, gaps in pricing to occur, bid/ask\r\nspreads to widen, and for the market to be volatile until the news is digested. Less experienced traders, by contrast, often expect business as\r\nusual. They expect their trades to be executed at the prices they see on\r\ntheir platforms and for their stops to be honored. In other words, they expect to get their orders filled at prices that may or may not exist or that\r\nare there for only a fraction of a second before moving. This often leads to\r\ncomplaints about orders not being executed or about so-called requotes.\r\nHowever, by the a time market order hits the broker’s server, the price\r\nmay no longer be there and in fact may have moved considerably from that\r\nlevel. A requote occurs when a market order is placed at a level that a broker cannot execute.\r\nSome refer to this as slippage, but it may simply be a market issue when\r\nprices are changing at a rapid pace. Brokers do not control the market\r\npricing mechanism and base their quotes around what is currently trading\r\nin the wholesale (interbank) market. Some brokers attempt to maintain\r\nfixed spreads, whereas others widen their bid/ask spread to reflect what is\r\nactually trading in the interbank market. This is not an attempt to defend\r\nbroker practices; rather, it is an effort to educate traders, especially the\r\nless experienced ones, about the workings of the market. No firm could\r\nafford to provide gap insurance in periods of volatility when prices have\r\ndisappeared in the interbank market. Some brokers tried to offer this in\r\nthe early days of retail trading, but it is no longer a common practice and it\r\nis unrealistic to expect it.',
        video_url=None,
        course_id=5
    )

    lesson11 = Lesson(
        lesson_name='Market Orders',
        content='This brings up the issue of market orders. A market order is the most common and basic type of order and is entered without a specific price limit\n(otherwise called a limit order). Once a market order is entered, the trader\nrelinquishes control over the price at which it will be filled. Essentially,\nthe trader is asking the broker or trading platform to execute the trade at\nthe best price available at that moment in time. This also brings up a point\nabout placing actual stops versus using mental stops, which is illustrated\nin a post from the Global-View forums:\n... nothing wrong with mental stops as long as you are very disciplined in executing them. Having said that, you run the risk of\ngiving yourself a really bad fill if some unexpected news comes out\nor your computer goes down, etc. Why not just leave the orders with\nthe broker?\nDuring normal times, the execution price should be close to the levels prevailing at the time the order is placed. However, during times of\nincreased volatility, such as right after a news event, the price at which\nthe order is executed (whether it be a buy or a sell) might be significantly\ndifferent than the quoted price at the time the order was placed. Those\nwho place market orders after a news event are leaving themselves at\nthe mercy of the market. Sometimes they can get lucky with a good fill,\nbut other times they may not be as lucky. The same is true for stop entry\norders placed to try to catch a directional move after a news event, as the\nexecution level could be significantly different from that specified in the\norder.\nTRADING THE NEWS—COMPLEX\nAND RISKY\nA full chapter could be written about the various combinations of reactions\nthat can take place after a news event. Sometimes the market will react and\nsustain a move. Other times, it may react briefly in one direction and then\nreverse. Some traders prefer to sit out trading news events and rather use\nthe way the market reacts as a clue to underlying strength or weakness of\na specific currency. There is a saying in the market that “It is not the news\nbut the market reaction to news that tells the tale.”\r\n\r\nThus the ability of a currency to shrug off good news or rally despite\r\nbad news can send a signal to the astute trader. In addition, the market\r\nis ever changing, sometimes trading with the news, sometimes against it,\r\nand sometimes before it. Here is a useful observation by a trader from New\r\nZealand:\r\nTrading the release of fundamental figures is not the same as it was\r\na few years ago. The market used to react a lot more than it does now\r\nat the release of major fundamental news. There is a way to trade\r\nmajor figure releases that was put forward when the market used to\r\nbe more reactive.\r\nIt appears recently that the market reacts more before the fundamental release based on consensus opinion.',
        video_url=None,
        course_id=5
    )

    db.session.add_all([
        lesson1,
        lesson2,
        lesson3,
        lesson4,
        lesson5,
        lesson6,
        lesson7,
        lesson8,
        lesson9,
        lesson10,
        lesson11,
    ])
    db.session.commit()

    # Create quizzes
    quiz1 = Quiz(
        lesson_id=lesson1.id,
        quiz_topic='What is Forex?'
    )

    quiz2 = Quiz(
        lesson_id=lesson2.id,
        quiz_topic='Forex Terms and calculations'
    )

    quiz3 = Quiz(
        lesson_id=lesson3.id,
        quiz_topic='CFTC Warning'
    )

    quiz4 = Quiz(
        lesson_id=lesson4.id,
        quiz_topic='Key to success as a trader: Preserve your capital'
    )

    quiz5 = Quiz(
        lesson_id=lesson5.id,
        quiz_topic='What is leverage?'
    )

    quiz6 = Quiz(
        lesson_id=lesson6.id,
        quiz_topic='What is technical analysis?'
    )

    quiz7 = Quiz(
        lesson_id=lesson7.id,
        quiz_topic='Technical analysis landscape'
    )

    quiz8 = Quiz(
        lesson_id=lesson8.id,
        quiz_topic='Wha is fundamental analysis?'
    )

    quiz9 = Quiz(
        lesson_id=lesson9.id,
        quiz_topic='Interest Rates'
    )

    quiz10 = Quiz(
        lesson_id=lesson10.id,
        quiz_topic='Caveat Emptor'
    )

    quiz11 = Quiz(
        lesson_id=lesson11.id,
        quiz_topic='Market Orders'
    )

    db.session.add_all([
        quiz1,
        quiz2,
        quiz3,
        quiz4,
        quiz5,
        quiz6,
        quiz7,
        quiz8,
        quiz9,
        quiz10,
        quiz11,
    ])
    db.session.commit()

    # Create questions
    q1 = Question(
        quiz_id=quiz1.id,
        question_text='Is a currency trade between two currencies called a "cross" if one of those currencies is the U.S. dollar (USD)?',
        option1='No',
        option2='Yes',
        option3=None,
        option4=None,
        correct_option='No'
    )

    q2 = Question(
        quiz_id=quiz1.id,
        question_text='True or False: There is a central clearinghouse for currency trading, similar to how stocks and commodity futures operate.',
        option1='False',
        option2='True',
        option3=None,
        option4=None,
        correct_option='False'
    )

    q3 = Question(
        quiz_id=quiz1.id,
        question_text='Does standard forex trading typically work off a bid/ask spread rather than charging traditional commissions or exchange fees?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='Yes'
    )

    q4 = Question(
        quiz_id=quiz1.id,
        question_text='Is it possible to trade forex 24 hours a day continuously from late Sunday afternoon to late Friday evening (U.S. time)?',
        option1='No',
        option2='Yes',
        option3=None,
        option4=None,
        correct_option='Yes'
    )

    q5 = Question(
        quiz_id=quiz1.id,
        question_text='According to the text, what does it mean to be "long" on the EUR/USD currency pair?',
        option1='You want the EUR to go down and the USD to go up',
        option2='You want the EUR to go up and the USD to go down',
        option3='You expect both currencies to remain completely stable',
        option4=None,
        correct_option='You want the EUR to go up and the USD to go down'
    )

    q6 = Question(
        quiz_id=quiz1.id,
        question_text='What is the standard lot size in retail FOREX according to the passage?',
        option1='100 units',
        option2='10,000 units',
        option3='100,000 units',
        option4=None,
        correct_option='100,000 units'
    )

    q7 = Question(
        quiz_id=quiz2.id,
        question_text='In a currency quotation, is the bid price displayed on the right-hand side?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='No'
    )

    q8 = Question(
        quiz_id=quiz2.id,
        question_text='True or False: The British pound, Eurozone euro, Australian dollar, and New Zealand dollar are primary exceptions to the rule that the U.S. dollar is normally the base currency in quotes.',
        option1='True',
        option2='False',
        option3=None,
        option4=None,
        correct_option='True'
    )

    q9 = Question(
        quiz_id=quiz2.id,
        question_text='Does the term "flat" or "square" describe a trader who holds a large open position in the market?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='No'
    )

    q10 = Question(
        quiz_id=quiz2.id,
        question_text='Is a leverage ratio of 100:1 considered low leverage for a new trader according to the text?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='No'
    )

    q11 = Question(
        quiz_id=quiz2.id,
        question_text='What is the second listed currency in a currency pair called?',
        option1='Base currency',
        option2='Counter currency',
        option3='Primary currency',
        option4=None,
        correct_option='Counter currency'
    )

    q12 = Question(
        quiz_id=quiz2.id,
        question_text='What dealer expression refers to omitting the first few digits of an exchange rate when quoting verbally (e.g., quoting 117.30/117.35 as “30/35”)?',
        option1='Big figure quote',
        option2='Fractional quote',
        option3='Spread quote',
        option4=None,
        correct_option='Big figure quote'
    )

    q13 = Question(
        quiz_id=quiz2.id,
        question_text='How is the relationship between Leverage and Margin Percent calculated?',
        option1='Leverage = Margin Percent × 100',
        option2='Leverage = 100 ÷ Margin Percent',
        option3='Leverage = Margin Percent ÷ 100',
        option4=None,
        correct_option='Leverage = 100 ÷ Margin Percent'
    )

    q14 = Question(
        quiz_id=quiz3.id,
        question_text='What is stated as the critical factor for remaining in the trading game?',
        option1='Maximum leverage',
        option2='Capital preservation',
        option3='Trading during every market session',
        option4=None,
        correct_option='Capital preservation'
    )

    q15 = Question(
        quiz_id=quiz3.id,
        question_text='What does the CFTC warning state regarding the money you invest in foreign exchange?',
        option1='You should only invest profits made from stock trading',
        option2='You should not invest money that you cannot afford to lose',
        option3='You are guaranteed to recover your initial capital over time',
        option4=None,
        correct_option='You should not invest money that you cannot afford to lose'
    )

    q16 = Question(
        quiz_id=quiz3.id,
        question_text='According to the text, is trading foreign exchange mainly about making money rather than capital preservation?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='No'
    )

    q17 = Question(
        quiz_id=quiz3.id,
        question_text='True or False: Novice traders frequently use stop loss orders to protect their trading capital.',
        option1='True',
        option2='False',
        option3=None,
        option4=None,
        correct_option='False'
    )

    q18 = Question(
        quiz_id=quiz3.id,
        question_text="True or False: High leverage always works in a trader's favour by multiplying profits without increasing potential losses.",
        option1='True',
        option2='False',
        option3=None,
        option4=None,
        correct_option='False'
    )

    q19 = Question(
        quiz_id=quiz4.id,
        question_text='Is overleveraging trading capital identified as a common error among new traders?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='Yes'
    )

    q20 = Question(
        quiz_id=quiz4.id,
        question_text='True or False: In Jay Meisler’s account, the trader’s major loss began after taking a trade following the release of economic news.',
        option1='True',
        option2='False',
        option3=None,
        option4=None,
        correct_option='True'
    )

    q21 = Question(
        quiz_id=quiz4.id,
        question_text='What is stated as goal number one for all traders, from small individuals to large hedge fund managers?',
        option1='Maximising leverage on every trade',
        option2='Capital preservation',
        option3='Earning at least 100 pips daily',
        option4=None,
        correct_option='Capital preservation'
    )

    q22 = Question(
        quiz_id=quiz4.id,
        question_text='What is usually the root source of the problem when traders are about to blow their accounts?',
        option1='High broker commissions',
        option2='A lack of discipline that turns a manageable loss into a crisis',
        option3='Unexpected movements in stock markets',
        option4=None,
        correct_option='A lack of discipline that turns a manageable loss into a crisis'
    )

    q23 = Question(
        quiz_id=quiz4.id,
        question_text='In the example provided, what replaced solid analysis when the trade began moving in the wrong direction?',
        option1='Hope',
        option2='Automation',
        option3='Hedging',
        option4=None,
        correct_option='Hope'
    )

    q24 = Question(
        quiz_id=quiz5.id,
        question_text='True or False: A margin deposit acts as a limit on the potential loss you can experience on a trade.',
        option1='True',
        option2='False',
        option3=None,
        option4=None,
        correct_option='False'
    )

    q25 = Question(
        quiz_id=quiz5.id,
        question_text='Does trading on a leveraged basis amplify both potential trading gains and potential trading losses?',
        option1='Yes',
        option2='No',
        option3=None,
        option4=None,
        correct_option='Yes'
    )

    q26 = Question(
        quiz_id=quiz5.id,
        question_text='How is a margin deposit best described in the text?',
        option1='A non-refundable service fee',
        option2='Good-faith or earnest money',
        option3='The maximum loss allowed on a trade',
        option4=None,
        correct_option='Good-faith or earnest money'
    )

    q27 = Question(
        quiz_id=quiz5.id,
        question_text='What formula is used in the text to calculate Leverage?',
        option1='Leverage = Required Margin ÷ Trading Position',
        option2='Leverage = Trading Position ÷ Required Margin',
        option3='Leverage = Exchange Rate × Required Margin',
        option4=None,
        correct_option='Leverage = Trading Position ÷ Required Margin'
    )

    q28 = Question(
        quiz_id=quiz5.id,
        question_text='Based on the example in the text, if a trader controls a $148,000 position with a $500 required margin, what is the leverage ratio?',
        option1='65:1',
        option2='200:1',
        option3='296:1',
        option4=None,
        correct_option='296:1'
    )

    db.session.add_all([
        q1,
        q2,
        q3,
        q4,
        q5,
        q6,
        q7,
        q8,
        q9,
        q10,
        q11,
        q12,
        q13,
        q14,
        q15,
        q16,
        q17,
        q18,
        q19,
        q20,
        q21,
        q22,
        q23,
        q24,
        q25,
        q26,
        q27,
        q28,
    ])
    db.session.commit()

    print('Database seeded successfully!')