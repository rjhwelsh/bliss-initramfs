# Copyright 2012-2014 Jonathan Vasquez <jvasquez1011@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pkg.hooks.hook import Hook

class Firmware(Hook):
    def __init__(self):
        Hook.__init__(self)

        # Copying firmware is disabled by default since the initramfs size can grow extremely quickly
        self.use = 0

        # If enabled, all the firmware in /lib/firmware will be copied into the initramfs.
        # If you know exactly what firmware files you want, definitely leave this at 0 so
        # to reduce the initramfs size.
        self.copy_all = 0

        # A list of firmware files to include in the initramfs
        self.files = [
            # Add your firmware files below
            #"/lib/firmware/iwlwifi-6000g2a-6.ucode",
            #"/lib/firmware/yamaha/yss225_registers.bin",
        ]

    # Gets the flag_all_firmware value
    def is_copy_all(self):
        return self.copy_all