# -*- coding:UTF-8 -*-
__author__ = 'lilei'

from models.MainModel import Model
from views.MainView import View, ChangerWidget

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view1 = View(root)
        self.view1.moneyCtrl.config(textvariable=self.model.myMoney)
        self.view2 = ChangerWidget(self.view1)
        self.view2.addButton.config(command=self.AddMoney)
        self.view2.removeButton.config(command=self.RemoveMoney)

    def AddMoney(self):
        self.model.addMoney(10)

    def RemoveMoney(self):
        self.model.removeMoney(10)