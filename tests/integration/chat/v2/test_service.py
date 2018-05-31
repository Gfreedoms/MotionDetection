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


class ServiceTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "limits": {
                    "channel_members": 100,
                    "user_channels": 250
                },
                "links": {
                    "channels": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels",
                    "users": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",
                    "roles": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",
                    "bindings": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings"
                },
                "notifications": {},
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "pre_webhook_retry_count": 2,
                "post_webhook_retry_count": 3,
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "media": {
                    "size_limit_mb": 150,
                    "compatibility_message": "media compatibility message"
                }
            }
            '''
        ))

        actual = self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services.create(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://chat.twilio.com/v2/Services',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "limits": {
                    "channel_members": 100,
                    "user_channels": 250
                },
                "links": {
                    "channels": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels",
                    "users": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",
                    "roles": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",
                    "bindings": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings"
                },
                "notifications": {},
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "pre_webhook_retry_count": 2,
                "post_webhook_retry_count": 3,
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "media": {
                    "size_limit_mb": 150,
                    "compatibility_message": "media compatibility message"
                }
            }
            '''
        ))

        actual = self.client.chat.v2.services.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://chat.twilio.com/v2/Services',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://chat.twilio.com/v2/Services?PageSize=50&Page=0",
                    "key": "services",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services?PageSize=50&Page=0"
                },
                "services": []
            }
            '''
        ))

        actual = self.client.chat.v2.services.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://chat.twilio.com/v2/Services?PageSize=50&Page=0",
                    "key": "services",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services?PageSize=50&Page=0"
                },
                "services": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "consumption_report_interval": 100,
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "friendly_name",
                        "limits": {
                            "channel_members": 100,
                            "user_channels": 250
                        },
                        "links": {
                            "channels": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels",
                            "users": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",
                            "roles": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",
                            "bindings": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings"
                        },
                        "notifications": {},
                        "post_webhook_url": "post_webhook_url",
                        "pre_webhook_url": "pre_webhook_url",
                        "pre_webhook_retry_count": 2,
                        "post_webhook_retry_count": 3,
                        "reachability_enabled": false,
                        "read_status_enabled": false,
                        "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "typing_indicator_timeout": 100,
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "webhook_filters": [
                            "webhook_filters"
                        ],
                        "webhook_method": "webhook_method",
                        "media": {
                            "size_limit_mb": 150,
                            "compatibility_message": "media compatibility message"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.chat.v2.services.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://chat.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "consumption_report_interval": 100,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "default_channel_creator_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_channel_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "default_service_role_sid": "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "friendly_name",
                "limits": {
                    "channel_members": 500,
                    "user_channels": 600
                },
                "links": {
                    "channels": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels",
                    "users": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users",
                    "roles": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Roles",
                    "bindings": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Bindings"
                },
                "notifications": {
                    "log_enabled": true,
                    "added_to_channel": {
                        "enabled": false,
                        "template": "notifications.added_to_channel.template"
                    },
                    "invited_to_channel": {
                        "enabled": false,
                        "template": "notifications.invited_to_channel.template"
                    },
                    "new_message": {
                        "enabled": false,
                        "template": "notifications.new_message.template",
                        "badge_count_enabled": true
                    },
                    "removed_from_channel": {
                        "enabled": false,
                        "template": "notifications.removed_from_channel.template"
                    }
                },
                "post_webhook_url": "post_webhook_url",
                "pre_webhook_url": "pre_webhook_url",
                "pre_webhook_retry_count": 2,
                "post_webhook_retry_count": 3,
                "reachability_enabled": false,
                "read_status_enabled": false,
                "sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "typing_indicator_timeout": 100,
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "webhook_filters": [
                    "webhook_filters"
                ],
                "webhook_method": "webhook_method",
                "media": {
                    "size_limit_mb": 150,
                    "compatibility_message": "new media compatibility message"
                }
            }
            '''
        ))

        actual = self.client.chat.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)
