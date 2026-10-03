"""
MailGuard Enterprise API - Disposable and Burner Email Domain Database
"""

DISPOSABLE_DOMAINS = {
    # Top 300+ most active disposable email services
    "mailinator.com", "10minutemail.com", "tempmail.com", "guerrillamail.com",
    "yopmail.com", "trashmail.com", "getairmail.com", "dispostable.com",
    "sharklasers.com", "guerrillamail.net", "guerrillamail.org", "guerrillamail.biz",
    "grr.la", "spam4.me", "nada.ltd", "dropmail.me", "mohmal.com", "fakemailgenerator.com",
    "temp-mail.org", "throwawaymail.com", "burnermail.io", "maildrop.cc",
    "mytemp.email", "getnada.com", "crazymailing.com", "emailondeck.com",
    "inboxkitten.com", "harakirimail.com", "trashmail.net", "trashmail.me",
    "mailcatch.com", "discard.email", "spambox.us", "jetable.org",
    "tempinbox.com", "kasmail.com", "binkmail.com", "bobmail.info",
    "chacuo.net", "devnullmail.com", "dodgeit.com", "dontsendmespam.de",
    "dumpmail.de", "e4ward.com", "emailias.com", "filzmail.com",
    "gishpuppy.com", "gowikicars.com", "haltospam.com", "hidemail.de",
    "incognitomail.org", "ipoo.org", "kasmail.com", "klzlk.com",
    "mailfreeonline.com", "mailmoat.com", "mailnull.com", "meltmail.com",
    "mintemail.com", "mycleaninbox.net", "noclickemail.com", "no-spam.ws",
    "nospam4.us", "nospamfor.us", "notsharingmy.info", "oneoffmail.com",
    "pookmail.com", "safetymail.info", "safetypost.de", "sendspamhere.com",
    "shieldmail.com", "shiftmail.com", "skeefmail.com", "slaskpost.se",
    "slopsbox.com", "sofort-mail.de", "sogetthis.com", "spam.la",
    "spamavert.com", "spambog.com", "spambog.de", "spambog.ru",
    "spamex.com", "spamfree24.org", "spamgourmet.com", "spamhole.com",
    "spaml.com", "spammotel.com", "spamspot.com", "spamtrap.ro",
    "spoofmail.de", "superstachel.de", "suremail.info", "tafmail.com",
    "tempemail.net", "temporaryforwarding.com", "temporaryinbox.com",
    "tempunblock.com", "timesavers.org", "tradermail.info", "trashinbox.com",
    "trbvm.com", "tuotu.com", "uggsrock.com", "veryrealemail.com",
    "vidalia.org", "walkmail.net", "wetrainbayarea.com", "whyspam.me",
    "willhackforfood.biz", "willselfdestruct.com", "winemaven.info",
    "wronghead.com", "wuzup.net", "xagloo.com", "xemaps.com",
    "xents.com", "xmaily.com", "xoxy.net", "yapped.net",
    "ypmail.webredirect.org", "yuurok.com", "zehnminutenmail.de",
    "zippymail.info", "zoemail.com", "zxcv.com", "zygotemail.com",
    "armyspy.com", "cuvox.de", "dayrep.com", "einrot.com",
    "fleckens.hu", "gustr.com", "jourrapide.com", "rhyta.com",
    "superrito.com", "teleworm.us", "fakeinbox.com", "generator.email",
    "trash-mail.com", "mohmal.im", "mohmal.in", "tutanota.com",
    "protonmail.com", "anonymousemail.me", "mailfence.com"
}

FREE_EMAIL_PROVIDERS = {
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "icloud.com",
    "aol.com", "zoho.com", "mail.com", "gmx.com", "yandex.com",
    "proton.me", "live.com", "msn.com", "comcast.net", "sbcglobal.net",
    "att.net", "verizon.net", "cox.net", "charter.net", "me.com",
    "mac.com", "bellsouth.net", "earthlink.net", "rediffmail.com",
    "web.de", "gmx.de", "t-online.de", "freenet.de", "mail.ru",
    "yandex.ru", "rambler.ru", "bk.ru", "inbox.ru", "list.ru",
    "orange.fr", "free.fr", "sfr.fr", "laposte.net", "wanadoo.fr",
    "libero.it", "virgilio.it", "alice.it", "tin.it", "uol.com.br",
    "bol.com.br", "terra.com.br", "ig.com.br", "yahoo.co.uk",
    "hotmail.co.uk", "btinternet.com", "virginmedia.com", "sky.com"
}

ROLE_BASED_PREFIXES = {
    "admin", "administrator", "info", "support", "sales", "billing",
    "contact", "help", "hello", "hi", "marketing", "jobs", "careers",
    "team", "office", "hr", "accounting", "press", "media", "feedback",
    "inquiries", "inquiry", "postmaster", "webmaster", "hostmaster",
    "abuse", "security", "privacy", "compliance", "legal", "dev",
    "development", "tech", "operations", "ops", "mail", "newsletter",
    "no-reply", "noreply", "donotreply", "auto", "automated", "service"
}

COMMON_DOMAIN_TYPOS = {
    "gmial.com": "gmail.com",
    "gmaill.com": "gmail.com",
    "gamil.com": "gmail.com",
    "gmai.com": "gmail.com",
    "gmal.com": "gmail.com",
    "yaho.com": "yahoo.com",
    "yahooo.com": "yahoo.com",
    "yaboo.com": "yahoo.com",
    "hotmial.com": "hotmail.com",
    "hotmaill.com": "hotmail.com",
    "hotmai.com": "hotmail.com",
    "outloo.com": "outlook.com",
    "outlok.com": "outlook.com",
    "iclud.com": "icloud.com",
    "icoud.com": "icloud.com"
}
