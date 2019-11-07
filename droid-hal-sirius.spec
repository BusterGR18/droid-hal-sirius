# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device sirius
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty MI 8 SE

%define installable_zip 1
%define droid_target_aarch64 1

%define android_config \
  #define WANT_ADRENO_QUIRKS 1 \
%{nil}

%define straggler_files \
/bt_firmware\
/bugreports\
/cache\
/d\
/dsp\
/etc\
/firmware\
/odm\
/persist\
/product\
/vendor\
%{nil}

%define makefstab_skip_entries /sys/fs/pstore

%include rpm/dhd/droid-hal-device.inc
