[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions required by the app (add necessary Android permissions here)
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (str) The package format to build for (android)
android.arch = armeabi-v7a

# (str) Target API for Android (adjust if necessary)
android.api = 33

# (int) Minimum API supported by the app
android.minapi = 21

# (str) Gradle version to use (required for GitHub CI environments)
android.gradle_dependencies = 'com.android.tools.build:gradle:7.0.0'

# (str) Build mode (debug/release)
android.debug = 1

# (str) Key alias and key password (for release builds; add to GitHub Secrets)
#android.release.keystore = ~/.keystore
#android.release.keyalias = my-key-alias
#android.release.password = my-key-password

# (bool) Whether to sign the APK for release
#android.sign_apk = 0

# (str) Path to the Java JDK (configure based on CI environment)
#android.sdk = /usr/lib/jvm/java-8-openjdk-amd64

# (str) Path to the Android NDK
#android.ndk_path = /opt/android-ndk

# (str) Enable build caching
android.enable_build_cache = 1

# (str) Additional gradle arguments (in case you need specific behavior)
#android.gradle_args = --no-daemon

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
# build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin
