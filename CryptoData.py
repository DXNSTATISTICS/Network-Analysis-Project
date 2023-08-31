#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:27:40 2023

@author: dixons
"""

from tvDatafeed import TvDatafeed, Interval
import pandas as pd
#import scipy.stats as stats
#import talib
#import pandas_ta as ta
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

tv = TvDatafeed()

#Currenies
# 1: BTC, 2: BCH, 3: DAI, 4: DOGE, 5: ELON, 6: LTC, 7: MIM, 8: PAXG, 9: SHIB, 10: USDC, 11: ZEC
dfBTC = tv.get_hist(symbol = 'BTCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfBCH = tv.get_hist(symbol = 'BCHUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfDAI = tv.get_hist(symbol = 'DAIUSD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfDOGE = tv.get_hist(symbol = 'DOGEUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfELON = tv.get_hist(symbol = 'ELONUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfLTC = tv.get_hist(symbol = 'LTCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMIM = tv.get_hist(symbol = 'MIMUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfPAXG = tv.get_hist(symbol = 'PAXGUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSHIB = tv.get_hist(symbol = 'SHIBUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfUSDC = tv.get_hist(symbol = 'USDCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfZEC = tv.get_hist(symbol = 'ZECUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)


dfUSDC.columns


#L1 L2 Platforms
#1: ETH, 2: FTM,3: KP3R, 4: LUNA, 5: MATIC, 6: QNT, 7: REN, 8: SKL, 9: SOL, 10: XTZ
dfETH = tv.get_hist(symbol = 'ETHUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfFTM = tv.get_hist(symbol = 'FTMUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfKP3R = tv.get_hist(symbol = 'KP3RUSD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfLUNA = tv.get_hist(symbol = 'LUNAUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMATIC = tv.get_hist(symbol = 'MATICUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfQNT = tv.get_hist(symbol = 'QNTUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfREN = tv.get_hist(symbol = 'RENUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSKL = tv.get_hist(symbol = 'SKLUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSOL = tv.get_hist(symbol = 'SOLUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfXTZ = tv.get_hist(symbol = 'XTZUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)

#DEFI
#1: 1INCH, 2: AAVE, 3: ALCX, 4: BAL, 5: BNT, 6: BOND, 7: COMP, 8: CRV, 9: CTX, 10: INJ, 11: KNC, 12: LRC, 13: MCO2
df1INCH = tv.get_hist(symbol = '1INCHUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfAAVE = tv.get_hist(symbol = 'AAVEUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfALCX = tv.get_hist(symbol = 'ALCXUSD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfBAL = tv.get_hist(symbol = 'BALUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfBNT = tv.get_hist(symbol = 'BNTUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfBOND = tv.get_hist(symbol = 'BONDUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfCOMP = tv.get_hist(symbol = 'COMPUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfCRV = tv.get_hist(symbol = 'CRVUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfCTX = tv.get_hist(symbol = 'CTXUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfINJ = tv.get_hist(symbol = 'INJUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfKNC = tv.get_hist(symbol = 'KNCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfLRC = tv.get_hist(symbol = 'LRCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMCO2 = tv.get_hist(symbol = 'MCO2USD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)

#WEB3
#1: AMP, 2: ANKR, 3: API3, 4: AUDIO, 5: AXS, 6: BAT, 7: CVC, 8: ENJ, 9: ENS, 10: FET, 
#11: FIL, 12: GALA, 13: GRT, 14: LINK, 15: LPT, 16: MASK, 17: MC, 18: OXT, 19: RAD, 20: RNDR, 21: SLP, 22: STORJ
dfAMP = tv.get_hist(symbol = 'AMPUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfANKR = tv.get_hist(symbol = 'ANKRUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfAPI3 = tv.get_hist(symbol = 'API3USD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfAUDIO = tv.get_hist(symbol = 'AUDIOUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfAXS = tv.get_hist(symbol = 'AXSUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfBAT = tv.get_hist(symbol = 'BATUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfCVC = tv.get_hist(symbol = 'CVCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfENJ = tv.get_hist(symbol = 'ENJUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfENS = tv.get_hist(symbol = 'ENSUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfFET = tv.get_hist(symbol = 'FETUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfFIL = tv.get_hist(symbol = 'FILUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfGALA = tv.get_hist(symbol = 'GALAUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfGRT = tv.get_hist(symbol = 'GRTUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfLINK = tv.get_hist(symbol = 'LINKUSD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfLPT = tv.get_hist(symbol = 'LPTUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMASK = tv.get_hist(symbol = 'MASKUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMC = tv.get_hist(symbol = 'MCUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfOXT = tv.get_hist(symbol = 'OXTUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfRAD = tv.get_hist(symbol = 'RADUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfRNDR = tv.get_hist(symbol = 'RNDRUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSLP = tv.get_hist(symbol = 'SLPUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSTORJ = tv.get_hist(symbol = 'STORJUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)

#AGG META
#CUBE,MANA,SAND
dfCUBE = tv.get_hist(symbol = 'CUBEUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfMANA = tv.get_hist(symbol = 'MANAUSD', exchange='GEMINI',interval = Interval.in_daily, n_bars = 5000)
dfSAND = tv.get_hist(symbol = 'SANDUSD', exchange= 'GEMINI',interval = Interval.in_daily, n_bars = 5000)

#Currenies
# 1: BTC, 2: BCH, 3: DAI, 4: DOGE, 5: ELON, 6: LTC, 7: MIM, 8: PAXG, 9: SHIB, 10: USDC, 11: ZEC

#L1 L2 Platforms
#1: ETH, 2: FTM,3: KP3R, 4: LUNA, 5: MATIC, 6: QNT, 7: REN, 8: SKL, 9: SOL, 10: XTZ
'ETH': dfETH['close'],
'FTM': dfFTM['close'],
'KP3R': dfKP3R['close'],
'LUNA': dfLUNA['close'],
'MATIC': dfMATIC['close'],
'QNT': dfQNT['close'],
'REN': dfREN['close'],
'SKL': dfSKL['close'],
'SOL': dfSOL['close'],
'XTZ': dfXTZ['close'],
 

#DEFI
#1: 1INCH, 2: AAVE, 3: ALCX, 4: BAL, 5: BNT, 6: BOND, 7: COMP, 8: CRV, 9: CTX, 10: INJ, 11: KNC, 12: LRC, 13: MCO2
'1INCH': df1INCH['close'],
'AAVE': dfAAVE['close'],
'ALCX': dfALCX['close'],
'BAL': dfBAL['close'],
'BNT': dfBNT['close'],
'BOND': dfBOND['close'],
'COMP': dfCOMP['close'],
'CRV': dfCRV['close'],
'CTX': dfCTX['close'],
'INJ': dfINJ['close'],
'KNC': dfKNC['close'],
'LRC': dfLRC['close'],
'MCO2': dfXTZ['close'],

#WEB3
#1: AMP, 2: ANKR, 3: API3, 4: AUDIO, 5: AXS, 6: BAT, 7: CVC, 8: ENJ, 9: ENS, 10: FET, 
#11: FIL, 12: GALA, 13: GRT, 14: LINK, 15: LPT, 16: MASK, 17: MC, 18: OXT, 19: RAD, 20: RNDR, 21: SLP, 22: STORJ
'AMP': dfAMP['close'],
'ANKR': dfANKR['close'],
'API3': dfAPI3['close'],
'AUDIO': dfAUDIO['close'],
'AXS': dfAXS['close'],
'BAT': dfBAT['close'],
'CVC': dfCVC['close'],
'ENJ': dfENJ['close'],
'ENS': dfENS['close'],
'FET': dfFET['close'],
'FIL': dfFIL['close'],
'GALA': dfGALA['close'],
'GRT': dfGRT['close'],
'LINK': dfLINK['close'],
'LPT': dfLPT['close'],
'MASK': dfMASK['close'],
'MC': dfMC['close'],
'OXT': dfOXT['close'],
'RAD': dfRAD['close'],
'RNDR': dfRNDR['close'],
'SLP': dfSLP['close'],
'STORJ': dfSTORJ['close'],

#AGG META
#CUBE,MANA,SAND
'CUBE': dfCUBE['close'],
'MANA': dfMANA['close'],
'SAND': dfSAND['close'],

dfALL = pd.DataFrame({'BTC': dfBTC['close'].diff(),
                      'BCH': dfBCH['close'].diff(),
                      'DAI': dfDAI['close'].diff(),
                      'DOGE': dfDOGE['close'].diff(),
                      'ELON': dfELON['close'].diff(),
                      'LTC': dfLTC['close'].diff(),
                      #'MIM': dfMIM['close'].diff(),
                      'PAXG': dfPAXG['close'].diff(),
                      'SHIB': dfSHIB['close'].diff(),
                      'USDC': dfUSDC['close'].diff(),
                      'ZEC': dfZEC['close'].diff(),
                      'ETH': dfETH['close'].diff(),
                      'FTM': dfFTM['close'].diff(),
                      'KP3R': dfKP3R['close'].diff(),
                      'LUNA': dfLUNA['close'].diff(),
                      'MATIC': dfMATIC['close'].diff(),
                      'QNT': dfQNT['close'].diff(),
                      'REN': dfREN['close'].diff(),
                      'SKL': dfSKL['close'].diff(),
                      'SOL': dfSOL['close'].diff(),
                      'XTZ': dfXTZ['close'].diff(),
                      '1INCH': df1INCH['close'].diff(),
                      'AAVE': dfAAVE['close'].diff(),
                      'ALCX': dfALCX['close'].diff(),
                      'BAL': dfBAL['close'].diff(),
                      'BNT': dfBNT['close'].diff(),
                      'BOND': dfBOND['close'].diff(),
                      'COMP': dfCOMP['close'].diff(),
                      'CRV': dfCRV['close'].diff(),
                      'CTX': dfCTX['close'].diff(),
                      'INJ': dfINJ['close'].diff(),
                      'KNC': dfKNC['close'].diff(),
                      'LRC': dfLRC['close'].diff(),
                      'MCO2': dfXTZ['close'].diff(),
                      'AMP': dfAMP['close'].diff(),
                      'ANKR': dfANKR['close'].diff(),
                      'API3': dfAPI3['close'].diff(),
                      'AUDIO': dfAUDIO['close'].diff(),
                      'AXS': dfAXS['close'].diff(),
                      'BAT': dfBAT['close'].diff(),
                      'CVC': dfCVC['close'].diff(),
                      'ENJ': dfENJ['close'].diff(),
                      'ENS': dfENS['close'].diff(),
                      'FET': dfFET['close'].diff(),
                      'FIL': dfFIL['close'].diff(),
                      'GALA': dfGALA['close'].diff(),
                      'GRT': dfGRT['close'].diff(),
                      'LINK': dfLINK['close'].diff(),
                      'LPT': dfLPT['close'].diff(),
                      'MASK': dfMASK['close'].diff(),
                      'MC': dfMC['close'].diff(),
                      'OXT': dfOXT['close'].diff(),
                      'RAD': dfRAD['close'].diff(),
                      'RNDR': dfRNDR['close'].diff(),
                      'SLP': dfSLP['close'].diff(),
                      'STORJ': dfSTORJ['close'].diff(),
                      'CUBE': dfCUBE['close'].diff(),
                      'MANA': dfMANA['close'].diff(),
                      'SAND': dfSAND['close'].diff()})

dfALL = dfALL.dropna()
dfALL

# An assets Covariance to Itself is the Variance
dfCOV = dfALL.cov()
dfCOV.to_excel('Cov2.xlsx')
# An assets correlation to itself is 1
dfCORR = dfALL.corr()

#dfALL.to_excel('All.xlsx')
#dfCOV.to_excel('COV.xlsx')
#dfCORR.to_excel('CORR.xlsx')

Labels = dfCORR.columns
Labels

#H7*u^1730HHgayey&&&!

#NETWORK X
#Create Graph Object
G = nx.Graph()


# Add nodes and edges to the graph
for crypto1 in dfCOV.index:
    for crypto2 in dfCOV.columns:
        if crypto1 != crypto2:
            weight = dfCOV.loc[crypto1, crypto2]
            G.add_edge(crypto1, crypto2, weight=weight)

# Draw the graph using a circular layout
plt.figure(figsize=(10, 10))
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10, font_weight='bold', node_color='lightblue', edge_color='gray')

# Draw edge labels
labels = nx.get_edge_attributes(G, 'weight')
for key in labels:
    labels[key] = f'{labels[key]:.6f}'
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

# Show the graph
plt.axis('off')
plt.title('Covariance Network Graph')
plt.show()

# =============================================================================
# =============================================================================
# # 
# =============================================================================
# =============================================================================
