Summary:	KWebGet is a frontend to wget.
Name:		kwebget
Version:	0.5
Release:	1
License:	GPL
Group:		X11/KDE/Applications
Group(pl):	X11/KDE/Aplikacje
Source0:	http://www.kpage.de/download/%{name}-%{version}.tar.bz2
URL:		http://www.kpage.de/en/kwebget/content.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
KWebGet is a frontend to wget.

%prep
%setup -q

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions"
LDFLAGS="-s"; export LDFLAGS
export CXXFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
