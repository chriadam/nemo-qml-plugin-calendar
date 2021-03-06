Name:       nemo-qml-plugin-calendar-qt5

Summary:    Calendar plugin for Nemo Mobile
Version:    0.1.4
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-calendar
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(libmkcal-qt5)
BuildRequires:  pkgconfig(libkcalcoren-qt5)
BuildRequires:  pkgconfig(libical)

%description
%{summary}.

%package tests
Summary:    QML calendar plugin tests
Group:      System/Libraries
BuildRequires:  pkgconfig(Qt5Test)
Requires:   %{name} = %{version}-%{release}

%description tests
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%qmake5 

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/calendar/libnemocalendar.so
%{_libdir}/qt5/qml/org/nemomobile/calendar/qmldir

%files tests
%defattr(-,root,root,-)
/opt/tests/nemo-qml-plugins-qt5/calendar/*
