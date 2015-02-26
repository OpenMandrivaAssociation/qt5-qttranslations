%define api 5
%define qtminor 4
%define qtsubminor 1

%define qtversion %{api}.%{qtminor}.%{qtsubminor}
%define qttarballdir qttranslations-opensource-src-%{qtversion}

Name:		qt5-qttranslations
Version:	%{qtversion}
Release:	1
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt-project.org
Source0:	http://download.qt-project.org/official_releases/qt/%{api}.%{qtminor}/%{version}/submodules/%{qttarballdir}.tar.xz
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist-tools
BuildRequires:	qt5-qttools
BuildArch:	noarch

%description
Translation files for Qt Project apps.

%files 
%{_qt5_translationsdir}

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5

%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
