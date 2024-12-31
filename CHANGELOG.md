# Changelog

All notable changes to this project will be documented in this file.

## What's new in ProcyonCLS 2025 2.3.0 Release Preview?

* Security Update - UB-20250000. (New Year update)

## What was new in ProcyonCLS 2025 2.2.0 Release Preview?

* Security Update - UB-20241227.

* Internal code refactoring.

* New update checker app (separate from Updater).

### WHat's the difference Update Checker and Updater?

The update checker application now performs update checks, whereas the updater app now will directly update the system. Why this change you may ask? Well previously, if a user checks for update, and if there wasn't any, the updater app would reboot the system, as it was launched not directly from kernel but as a standalone app, which was not the intended behavior. Now, the update checker app will check for updates, and if there are any, it will prompt the user to update the system, or else, we can resume working without need for rebooting unnecessarily.

## What was new in ProcyonCLS 2025 2.1.0 Release Preview?

* Security Update - UB-20241224.

* Internal improvements and bug fixes.

## What was new in ProcyonCLS 2025 2.0.5 Developer Preview 12?

* Security Update - UB-20241219.

## What was new in ProcyonCLS 2025 2.0.4 Developer Preview 12?

* Security Update - UB-20241213.

* Kernel API update.

## What was new in ProcyonCLS 2025 2.0.3 Developer Preview 12?

* Fixed Critical OOBE Flaw.

## What was new in ProcyonCLS 2025 2.0.2 Developer Preview 12?

* Fixed critical OOBE flaw.

## What was in ProcyonCLS 2025 2.0.1 Developer Preview 12?

* Security Update - UB-20241212.

* Revamped UI.

* Using `blessed` for UI.

## What was new in ProcyonCLS 2025 1.9.1 Developer Preview 10?

* Security Update - UB-20241211.

* File explorer enablement patch.

* Revamped shell.

## What was new in ProcyonCLS 2025 1.9.0 Developer Preview 10?

* Security Update - UB-20241210.

* Added new file explorer app.

## What was new in ProcyonCLS 2025 1.8.0 Developer Preview 10?

* Security Update - UB-20241209.

* Revamped security app.

* Added new importable kernel APIs.

## What was new in ProcyonCLS 2025 1.7.1 Developer Preview 10?

* Security Update - UB-20241207-4.

* Patched a critical vulnerability in the security app.