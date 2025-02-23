# -*- coding: utf-8 -*-
"""
Created on Sun Apr  19 16:31:19 2020

@author: intgridnb-02
"""
from .auxFunc import initializer


class MarketResults():
    
    @initializer
    def __init__(self,
                 name,
                 issuer="None",
                 confirmedBids=[],
                 rejectedBids=[],
                 partiallyConfirmedBids=[],
                 marketClearingPrice=9999,
                 marginalUnit="None",
                 energyDeficit=0,
                 energySurplus=0,
                 status="N/A",
                 timestamp="N/A"):
        """
        

        Parameters
        ----------
        name : TYPE
            DESCRIPTION.
        issuer : TYPE, optional
            DESCRIPTION. The default is "None".
        confirmedBids : TYPE, optional
            DESCRIPTION. The default is [].
        rejectedBids : TYPE, optional
            DESCRIPTION. The default is [].
        marketClearingPrice : TYPE, optional
            DESCRIPTION. The default is 9999.
        marginalUnit : TYPE, optional
            DESCRIPTION. The default is "None".
        energyDeficit : TYPE, optional
            DESCRIPTION. The default is 0.
        energySurplus : TYPE, optional
            DESCRIPTION. The default is 0.
        status : TYPE, optional
            DESCRIPTION. The default is "N/A".
        timestamp : TYPE, optional
            DESCRIPTION. The default is "N/A".

        Returns
        -------
        None.

        """
        self.feedback()

    def feedback(self):
        for bid in self.confirmedBids:
            bid.issuer.feedback(bid)
        for bid in self.partiallyConfirmedBids:
            bid.issuer.feedback(bid)
        for bid in self.rejectedBids:
            bid.issuer.feedback(bid)