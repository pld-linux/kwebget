# Note that this is NOT a relocatable package
%define ver      0.4
%define rel      1
%define prefix   /usr

Summary:   KWebGet is a frontend to wget.
Name:      kwebget
Version:   %ver
Release:   %rel
Copyright: GPL
Group:     X11/KDE/Applications
Source0:   kwebget-%{PACKAGE_VERSION}.tar.gz
BuildRoot: /tmp/kvolume-%{PACKAGE_VERSION}-root
Packager:  Nicolas Vignal <nicolas.vignal@fnac.net>
URL :	   http://www.kpage.de/en/kwebget/index.html
Docdir: %{prefix}/doc

%description
KWebGet is a frontend to wget.

%prep
rm -rf %{builddir}

%setup
touch `find . -type f`

%build
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$KDEDIR --with-install-root=$RPM_BUILD_ROOT
make

%install
if [ -z "$KDEDIR" ]; then
        export KDEDIR=%{prefix}
fi
rm -rf $RPM_BUILD_ROOT
make install-strip

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed -e 's,^\.,\%attr(-\,root\,root) ,' \
	-e '/\/config\//s|^|%config|' >> \
	$RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> \
	$RPM_BUILD_DIR/file.list.%{name}
echo "%docdir $KDEDIR/doc/kde" >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
