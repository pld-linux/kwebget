Summary:	KWebGet is a frontend to wget
Summary(pl.UTF-8):	KWebGet - frontend na wget
Name:		kwebget
Version:	0.8.1
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.kpage.de/download/%{name}-%{version}.tar.bz2
# Source0-md5:	0143a6e092da11000bafe6c71912247c
Source1:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source1-md5:	e5c75ce22f1525b13532b519ae88e7a4
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-am19.patch
URL:		http://www.kpage.de/en/kwebget/content.html
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KWebGet is a frontend to wget.

%description -l pl.UTF-8
KWegGet to frontend KDE na wget.

%prep
%setup -q -n %{name} -a1
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%{__make} -f admin/Makefile.common cvs
%configure \
	%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
	%endif
	--with-qt-libraries=%{_libdir} \
	--with-qt-includes=/usr/include/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_docdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Applications/kwebget.desktop,%{_desktopdir}}

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kwebget.desktop
%{_iconsdir}/hicolor/*/apps/*
