#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.01.95
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		merkuro
Summary:	Kalendar
Name:		ka5-%{kaname}
Version:	24.01.95
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ec7f37018e8bb92d4290fb41a629e93e
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6DBus-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel >= 5.15.2
BuildRequires:	Qt6Qml-devel >= 5.15.10
BuildRequires:	Qt6Quick-devel >= 5.15.10
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgme-c++-devel
BuildRequires:	gpgme-qt6-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-mimetreeparser-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= 5.96.0
BuildRequires:	kf6-kcalendarcore-devel >= 5.105.0
BuildRequires:	kf6-kcontacts-devel >= 5.105.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.96.0
BuildRequires:	kf6-ki18n-devel >= 5.109.0
BuildRequires:	kf6-kiconthemes >= 5.96.0
BuildRequires:	kf6-kirigami-devel >= 5.96.0
BuildRequires:	kf6-kitemmodels-devel >= 5.105.0
BuildRequires:	kf6-qqc2-desktop-style-devel >= 5.96.0
BuildRequires:	kirigami-addons-devel >= 0.7.2
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Merkuro is a Kirigami-based calendar and task management application
that uses Akonadi. It lets you add, edit and delete events and tasks
from local and remote accounts of your choice, while keeping changes
synchronised across your Plasma desktop or phone.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/merkuro-calendar
%attr(755,root,root) %{_bindir}/merkuro-contact
%attr(755,root,root) %{_bindir}/merkuro-mail
%{_libdir}/qt6/qml/org/kde/akonadi/AgentConfigurationForm.qml
%{_libdir}/qt6/qml/org/kde/akonadi/CollectionComboBox.qml
%{_libdir}/qt6/qml/org/kde/akonadi/MobileCollectionComboBox.qml
%{_libdir}/qt6/qml/org/kde/akonadi/TagManagerPage.qml
%{_libdir}/qt6/qml/org/kde/akonadi/libakonadi_quick_plugin.so
%{_libdir}/qt6/qml/org/kde/akonadi/qmldir
%dir %{_libdir}/qt6/qml/org/kde/merkuro
%dir %{_libdir}/qt6/qml/org/kde/merkuro/calendar
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/BottomToolBar.qml
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/PriorityComboBox.qml
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/ReminderDelegate.qml
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/libmerkuro_calendar_plugin.so
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/qmldir
%dir %{_libdir}/qt6/qml/org/kde/merkuro/components
%{_libdir}/qt6/qml/org/kde/merkuro/components/BaseApplication.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/ColoredCheckbox.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/EditMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/FileMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/HelpMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/KActionFromAction.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/KQuickCommandBarPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/NativeEditMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/NativeFileMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/NativeHelpMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/NativeMenuItemFromAction.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/NativeWindowMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/SettingsMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/ViewMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/WindowMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/components/libmerkuro_components_plugin.so
%{_libdir}/qt6/qml/org/kde/merkuro/components/qmldir
%dir %{_libdir}/qt6/qml/org/kde/merkuro/contact
%{_libdir}/qt6/qml/org/kde/merkuro/contact/AddressBookCollectionHandler.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/ContactChooserPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/ContactView.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/GlobalMenuBar.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/MenuBar.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/Sidebar.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/libmerkuro_contact_plugin.so
%dir %{_libdir}/qt6/qml/org/kde/merkuro/contact/private
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/AddressBookMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/ContactGroupPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/ContactListItem.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/ContactPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/ContactsPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/DeleteContactAction.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/Header.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/PhoneNumberDialog.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/QrCodePage.qml
%dir %{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/AddressBookEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/BusinessEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/ContactEditorPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/ContactGroupEditorPage.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/EmailEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/InstantMessengerEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/PersonalInfoEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/PhoneEditorCard.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/private/contact_editor/PhotoEditor.qml
%{_libdir}/qt6/qml/org/kde/merkuro/contact/qmldir
%dir %{_libdir}/qt6/qml/org/kde/merkuro/mail
%{_libdir}/qt6/qml/org/kde/merkuro/mail/ConversationViewer.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/FolderView.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/MailComposer.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/MailSidebar.qml
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/merkuro/mail/libmerkuro_mail_plugin.so
%dir %{_libdir}/qt6/qml/org/kde/merkuro/mail/mailboxselector
%{_libdir}/qt6/qml/org/kde/merkuro/mail/mailboxselector/MailBoxList.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/mailboxselector/MailBoxListPage.qml
%dir %{_libdir}/qt6/qml/org/kde/merkuro/mail/mailpartview
%{_libdir}/qt6/qml/org/kde/merkuro/mail/mailpartview/ICalPart.qml
%dir %{_libdir}/qt6/qml/org/kde/merkuro/mail/private
%{_libdir}/qt6/qml/org/kde/merkuro/mail/private/AttachmentDelegate.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/private/MailDelegate.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/qmldir
%{_libdir}/qt6/qml/org/kde/akonadi/akonadi_quick_plugin.qmltypes
%{_libdir}/qt6/qml/org/kde/akonadi/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/MenuBar.qml
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/merkuro/calendar/merkuro_calendar_plugin.qmltypes
%{_libdir}/qt6/qml/org/kde/merkuro/components/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/merkuro/components/merkuro_components_plugin.qmltypes
%{_libdir}/qt6/qml/org/kde/merkuro/contact/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/merkuro/contact/merkuro_contact_plugin.qmltypes
%{_libdir}/qt6/qml/org/kde/merkuro/mail/actions/DeleteFolderAction.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/actions/MailItemMenu.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/actions/NewFolderAction.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/desktopactions/openmbox.qml
%{_libdir}/qt6/qml/org/kde/merkuro/mail/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/merkuro/mail/merkuro_mail_plugin.qmltypes
%{_desktopdir}/org.kde.merkuro.calendar.desktop
%{_desktopdir}/org.kde.merkuro.contact.desktop
%{_desktopdir}/org.kde.merkuro.mail.desktop
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/metainfo/org.kde.merkuro.calendar.metainfo.xml
%{_datadir}/metainfo/org.kde.merkuro.contact.appdata.xml
%{_datadir}/metainfo/org.kde.merkuro.contact.metainfo.xml
%{_datadir}/metainfo/org.kde.merkuro.mail.metainfo.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.merkuro.contact
%dir %{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/config
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/config/main.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/resources
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/resources/fallbackBackground.png
%dir %{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/CompactRepresentation.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/ContactListItem.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/ContactPage.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/ContactsPage.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/Header.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/QrCodePage.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact/metadata.json.license
%{_datadir}/qlogging-categories6/akonadi.quick.categories
%{_datadir}/qlogging-categories6/merkuro.categories
%{_datadir}/qlogging-categories6/merkuro.contact.categories
