name: Build Android APK
on: [push, workflow_dispatch]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install Buildozer to generate spec file
        run: |
          pip install buildozer
          buildozer init

      - name: Build APK with Buildozer Action
        uses: ArtemGovorov/buildozer-action@v1
        with:
          workdir: .
          buildozer_version: master

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: Android-APK
          path: bin/*.apk
