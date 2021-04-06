%define beta %{nil}

Name:		qt5-qttranslations
Version:	5.15.3
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qttranslations-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qttranslations-everywhere-src-5.15.2
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/5.15.2/submodules/%{qttarballdir}.tar.xz
%endif
# From KDE
Patch1000:	0001-fix-translation-of-discard-in-italian.patch
Patch1002:	0003-add-croatian-translation.patch
Patch1005:	0006-Bump-version.patch
Patch1007:	0008-Add-pt_BR-translations-for-5.12.patch
Patch1008:	0009-Split-and-update-Persian-translations.patch
Patch1009:	0010-Add-dutch-nl-files-and-partial-translations.patch
Patch1010:	0011-update-chinese-simplifid-language-for-qt5.12.patch
Patch1011:	0012-l10n-zh_TW-update-translations.patch
Patch1012:	0013-Add-initial-translation-for-Norwegian-Nynorsk.patch
Patch1013:	0014-Remove-obsolete-entries-from-zh_CN-translations.patch
Patch1014:	0015-Update-pt_BR-translations-for-5.15-branch.patch
Patch1015:	0016-prune-bogus-comment-from-linguist_nl.patch
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5 >= %{version}
BuildRequires:	pkgconfig(Qt5Core) >= %{version}
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-qttools
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1
BuildArch:	noarch

%description
Translation files for Qt Project apps.

%files
%{_qt5_translationsdir}

#------------------------------------------------------------------------------

%prep
%autosetup -n %qttarballdir -p1
%{_libdir}/qt5/bin/syncqt.pl -version %{version}

%build
%qmake_qt5

%make_build

#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}
