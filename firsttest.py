#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import time
import random

class WordDiscrimination(wx.Frame):
    def __init__(self, parent, title):
        super(WordDiscrimination, self).__init__(parent, title=title, size=(400, 600))
        self.Centre()

        allWords = []
        with open('samplewords.txt', 'r') as f:
            for line in f:
                allWords.append(line)

        randomWords = []
        while len(randomWords) < 12:
            word = random.choice(allWords)
            if word not in randomWords:
                randomWords.append(word)

        panel = wx.Panel(self)
        self.yesButton = wx.Button(panel, label="Yes")
        self.noButton = wx.Button(panel, label="No")

        for randomWord in randomWords:
            font = wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.DEFAULT)
            self.wordPrompt = wx.StaticText(panel, label=randomWord, style=wx.ALIGN_CENTRE_HORIZONTAL)
            self.wordPrompt.SetFont(font)
            time.sleep(1.5)
        



app = wx.App()
test = WordDiscrimination(None, title="Word Discrimination")
test.Show()
app.MainLoop()

