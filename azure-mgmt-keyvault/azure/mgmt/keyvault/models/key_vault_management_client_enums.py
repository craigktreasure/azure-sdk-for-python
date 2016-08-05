# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class SkuFamily(Enum):

    a = "A"


class SkuName(Enum):

    standard = "standard"
    premium = "premium"


class KeyPermissions(Enum):

    all = "all"
    encrypt = "encrypt"
    decrypt = "decrypt"
    wrapkey = "wrapkey"
    unwrapkey = "unwrapkey"
    sign = "sign"
    verify = "verify"
    get = "get"
    list = "list"
    create = "create"
    update = "update"
    import_enum = "import"
    delete = "delete"
    backup = "backup"
    restore = "restore"


class SecretPermissions(Enum):

    all = "all"
    get = "get"
    list = "list"
    set = "set"
    delete = "delete"
