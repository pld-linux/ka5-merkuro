#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		merkuro
Summary:	Kalendar
Summary(pl.UTF-8):	Kalendarz
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0c34fafc556e25462acb3fdbe89d75aa
URL:		https://apps.kde.org/merkuro/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.15.2
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel >= 5.15.10
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	gpgmepp-devel
BuildRequires:	ka5-akonadi-calendar-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-kcalutils-devel >= %{kdeappsver}
BuildRequires:	ka5-kidentitymanagement-devel >= %{kdeappsver}
BuildRequires:	ka5-pimcommon-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.96.0
BuildRequires:	kf5-kcalendarcore-devel >= 5.105.0
BuildRequires:	kf5-kcontacts-devel >= 5.105.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.96.0
BuildRequires:	kf5-ki18n-devel >= 5.109.0
BuildRequires:	kf5-kiconthemes >= 5.96.0
BuildRequires:	kf5-kirigami2-devel >= 5.96.0
BuildRequires:	kf5-kirigami-addons-devel >= 0.7.2
BuildRequires:	kf5-kitemmodels-devel >= 5.105.0
BuildRequires:	kf5-qqc2-desktop-style-devel >= 5.96.0
BuildRequires:	ninja
BuildRequires:	qgpgme-qt5-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Merkuro is a Kirigami-based calendar and task management application
that uses Akonadi. It lets you add, edit and delete events and tasks
from local and remote accounts of your choice, while keeping changes
synchronised across your Plasma desktop or phone.

%description -l pl.UTF-8
Merkuro to oparty na Kirigami kalendarz i aplikacja do zarządzania
zadaniami, wykorzystująca Akonadi. Pozwala dodawać, modyfikować i
usuwać wydarzenia i zadania z wybranych lokalnych i zdalnych kont,
pilnując synchronizacji z pulpitem Plazmy lub telefonem.

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
# merkuro seems to be the only user of %{_libdir}/qt5/qml/org/kde/akonadi, move dir here? (from ka5-akonadi)
%{_libdir}/qt5/qml/org/kde/akonadi/AgentConfigurationForm.qml
%{_libdir}/qt5/qml/org/kde/akonadi/CollectionComboBox.qml
%{_libdir}/qt5/qml/org/kde/akonadi/IdentityConfigurationForm.qml
%{_libdir}/qt5/qml/org/kde/akonadi/MobileCollectionComboBox.qml
%{_libdir}/qt5/qml/org/kde/akonadi/TagManagerPage.qml
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/akonadi/libakonadi_quick_plugin.so
%{_libdir}/qt5/qml/org/kde/akonadi/qmldir
%dir %{_libdir}/qt5/qml/org/kde/merkuro
%dir %{_libdir}/qt5/qml/org/kde/merkuro/calendar
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/merkuro/calendar/libmerkuro_calendar_plugin.so
%{_libdir}/qt5/qml/org/kde/merkuro/calendar/*.qml
%{_libdir}/qt5/qml/org/kde/merkuro/calendar/qmldir
%dir %{_libdir}/qt5/qml/org/kde/merkuro/components
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/merkuro/components/libmerkuro_components_plugin.so
%{_libdir}/qt5/qml/org/kde/merkuro/components/*.qml
%{_libdir}/qt5/qml/org/kde/merkuro/components/qmldir
%dir %{_libdir}/qt5/qml/org/kde/merkuro/contact
%{_libdir}/qt5/qml/org/kde/merkuro/contact/private
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/merkuro/contact/libmerkuro_contact_plugin.so
%{_libdir}/qt5/qml/org/kde/merkuro/contact/*.qml
%{_libdir}/qt5/qml/org/kde/merkuro/contact/qmldir
%dir %{_libdir}/qt5/qml/org/kde/merkuro/mail
%{_libdir}/qt5/qml/org/kde/merkuro/mail/mailboxselector
%{_libdir}/qt5/qml/org/kde/merkuro/mail/mailpartview
%{_libdir}/qt5/qml/org/kde/merkuro/mail/private
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/merkuro/mail/libmerkuro_mail_plugin.so
%{_libdir}/qt5/qml/org/kde/merkuro/mail/*.qml
%{_libdir}/qt5/qml/org/kde/merkuro/mail/qmldir
%{_datadir}/metainfo/org.kde.merkuro.calendar.metainfo.xml
%{_datadir}/metainfo/org.kde.merkuro.contact.appdata.xml
%{_datadir}/metainfo/org.kde.merkuro.contact.metainfo.xml
%{_datadir}/metainfo/org.kde.merkuro.mail.metainfo.xml
%{_datadir}/plasma/plasmoids/org.kde.merkuro.contact
%{_datadir}/qlogging-categories5/akonadi.quick.categories
%{_datadir}/qlogging-categories5/merkuro.categories
%{_datadir}/qlogging-categories5/merkuro.contact.categories
%{_desktopdir}/org.kde.merkuro.calendar.desktop
%{_desktopdir}/org.kde.merkuro.contact.desktop
%{_desktopdir}/org.kde.merkuro.mail.desktop
%{_iconsdir}/hicolor/128x128/apps/org.kde.merkuro.calendar.png
%{_iconsdir}/hicolor/128x128/apps/org.kde.merkuro.contact.png
%{_iconsdir}/hicolor/128x128/apps/org.kde.merkuro.mail.png
%{_iconsdir}/hicolor/256x256/apps/org.kde.merkuro.calendar.png
%{_iconsdir}/hicolor/256x256/apps/org.kde.merkuro.contact.png
%{_iconsdir}/hicolor/256x256/apps/org.kde.merkuro.mail.png
%{_iconsdir}/hicolor/48x48/apps/org.kde.merkuro.calendar.png
%{_iconsdir}/hicolor/48x48/apps/org.kde.merkuro.contact.png
%{_iconsdir}/hicolor/48x48/apps/org.kde.merkuro.mail.png
