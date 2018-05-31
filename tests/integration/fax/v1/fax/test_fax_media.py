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


class FaxMediaTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                              .media(sid="MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://fax.twilio.com/v1/Faxes/FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media/MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "content_type": "application/pdf",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "fax_sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .media(sid="MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                              .media.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://fax.twilio.com/v1/Faxes/FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media',
        ))

    def test_read_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "media": [
                    {
                        "sid": "MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "fax_sid": "FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "content_type": "application/pdf",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media/MEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media?PageSize=50&Page=0",
                    "key": "media",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://fax.twilio.com/v1/Faxes/FXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Media?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .media.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                              .media(sid="MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://fax.twilio.com/v1/Faxes/FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media/MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.fax.v1.faxes(sid="FXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .media(sid="MEXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
