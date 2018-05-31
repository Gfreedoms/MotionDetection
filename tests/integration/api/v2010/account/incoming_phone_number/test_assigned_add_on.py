# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AssignedAddOnTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .assigned_add_ons(sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/IncomingPhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AssignedAddOns/XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "VoiceBase High Accuracy Transcription",
                "description": "Automatic Transcription and Keyword Extract...",
                "configuration": {
                    "bad_words": true
                },
                "unique_name": "voicebase_high_accuracy_transcription",
                "date_created": "Thu, 07 Apr 2016 23:52:28 +0000",
                "date_updated": "Thu, 07 Apr 2016 23:52:28 +0000",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "subresource_uris": {
                    "extensions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions.json"
                }
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .assigned_add_ons(sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .assigned_add_ons.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/IncomingPhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AssignedAddOns.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "assigned_add_ons": [
                    {
                        "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "resource_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "VoiceBase High Accuracy Transcription",
                        "description": "Automatic Transcription and Keyword Extract...",
                        "configuration": {
                            "bad_words": true
                        },
                        "unique_name": "voicebase_high_accuracy_transcription",
                        "date_created": "Thu, 07 Apr 2016 23:52:28 +0000",
                        "date_updated": "Thu, 07 Apr 2016 23:52:28 +0000",
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                        "subresource_uris": {
                            "extensions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions.json"
                        }
                    }
                ],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .assigned_add_ons.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "assigned_add_ons": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .assigned_add_ons.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .assigned_add_ons.create(installed_add_on_sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {'InstalledAddOnSid': "XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/IncomingPhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AssignedAddOns.json',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "resource_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "VoiceBase High Accuracy Transcription",
                "description": "Automatic Transcription and Keyword Extract...",
                "configuration": {
                    "bad_words": true
                },
                "unique_name": "voicebase_high_accuracy_transcription",
                "date_created": "Thu, 07 Apr 2016 23:52:28 +0000",
                "date_updated": "Thu, 07 Apr 2016 23:52:28 +0000",
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                "subresource_uris": {
                    "extensions": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AssignedAddOns/XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Extensions.json"
                }
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .assigned_add_ons.create(installed_add_on_sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .assigned_add_ons(sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/IncomingPhoneNumbers/PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/AssignedAddOns/XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts(sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .incoming_phone_numbers(sid="PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .assigned_add_ons(sid="XEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
