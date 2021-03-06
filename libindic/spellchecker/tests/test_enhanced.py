#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

from libindic.stemmer import Malayalam as stemmer
from testtools import TestCase
from io import open
from pkg_resources import resource_filename

from .. import Malayalam as spellchecker


class MalayalamSpellcheckerTest(TestCase):

    def open_resource(self, filename):
        fname = resource_filename("libindic.spellchecker.tests",
                                  "resources/" + filename)
        return open(fname, "r", encoding="utf-8")

    def setUp(self):
        super(MalayalamSpellcheckerTest, self).setUp()
        self.spellchecker = spellchecker()
        self.true_cases = self.open_resource("true.txt")
        self.false_cases = self.open_resource("false.txt")

    def test_check(self):
        for line in self.true_cases:
            word = line.strip()
            self.assertEqual(self.spellchecker.check(word), True)

        for line in self.false_cases:
            word = line.strip()
            self.assertEqual(self.spellchecker.check(word), False)

    def test_suggest(self):
        pass
