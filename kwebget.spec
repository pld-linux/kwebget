Summary:	KWebGet is a frontend to wget
Summary(pl):	KWebGet - frontend na wget
Name:		kwebget
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(cs):	X11/Aplikace/Sí»ové
Group(da):	X11/Programmer/Netværks
Group(de):	X11/Applikationen/Netzwerkwesen
Group(es):	X11/Aplicaciones/Red
Group(fr):	X11/Applications/Réseau
Group(is):	X11/Forrit/Net
Group(it):	X11/Applicazioni/Rete
Group(no):	X11/Applikasjoner/Nettverks
Group(pl):	X11/Aplikacje/Sieciowe
Group(pt_BR):	X11/Aplicações/Rede
Group(pt):	X11/Aplicações/Rede
Group(ru):	X11/ðÒÉÌÏÖÅÎÉÑ/óÅÔÅ×ÙÅ
Group(sl):	X11/Programi/Omre¾ni
Group(sv):	X11/Tillämpningar/Nätverk
Source0:	http://www.kpage.de/download/%{name}-%{version}.tar.bz2
URL:		http://www.kpage.de/en/kwebget/content.html
BuildRequires:	kdelibs-devel >= 2.0
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define         _htmldir        /usr/share/doc/kde/HTML

%description
KWebGet is a frontend to wget.

%description -l pl
KWegGet to frontend KDE na wget.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13 \
	--with-qt-includes=/usr/X11R6/include/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Internet,Network}

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Network/kwebget.desktop
%{_pixmapsdir}/*/*/apps/*
