# firefox2keepassx
Converts your Firefox passwords to KeePassX format

1. Open Firefox, install Password Exporter addon

    https://addons.mozilla.org/en-us/firefox/addon/password-exporter/

2. Export your passwords to xml file, rename it as `data.xml`

3. Launch Python script to convert to keepassx format

        python convert.py

4. Import the generated `out.xml` file to KeePassX: File -> Import from -> KeePassX XML
