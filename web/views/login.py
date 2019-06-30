# coding: utf-8
#

from logzero import logger
import os

from .auth import AuthError, OpenIdMixin
from .base import BaseRequestHandler

from ..settings import AUTH_BACKENDS


class OpenIdLoginHandler(BaseRequestHandler, OpenIdMixin):
    _OPENID_ENDPOINT = AUTH_BACKENDS['openid']['endpoint']

    async def get(self):
        if self.get_argument("openid.mode", False):
            try:
                user = await self.get_authenticated_user()
            except AuthError as e:
                self.write(
                    "<code>Auth error: {}</code> <a href='/login'>Login</a>".
                    format(e))
            else:
                logger.info("User info: %s", user)
                await self.set_current_user(user['email'], user['name'])
                next_url = self.get_argument('next', '/')
                self.redirect(next_url)
        else:
            self.authenticate_redirect()


class SimpleLoginHandler(BaseRequestHandler):
    def get(self):
        self.set_cookie("next", self.get_argument("next", "/"))
        cwd = os.getcwd()
        self.write('<html><body>'
        '<center>'
        '<img src="https://imagizer.imageshack.com/img924/2135/19C3kS.png" style="width:384px;height:221px;">'
        '<form action="/login" method="post">'
                   'Login: <input type="text" name="name" required>'
                   '<input type="submit" value="Sign in">'
                   '</form></center></body></html>')

    async def post(self):
        name = self.get_argument("name")
        email = name + "@anonymous.com"
        await self.set_current_user(email, name)
        next_url = self.get_cookie("next", "/")
        self.clear_cookie("next")
        self.redirect(next_url)
