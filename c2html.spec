Summary:	C2html - Converts C files to HTML
Summary(pl):	C2html - konwerter ¼róde³ C na HTML
Name:		c2html
Version:	0.9.5
Release:	1
Epoch:		0
License:	GPL
Group:		Applications/Text
Source0:	http://user.cs.tu-berlin.de/~schintke/x2html/%{name}-%{version}.tar.gz
# Source0-md5:	324cd6c50dd611607e3366840bbc61f2
Patch0:		%{name}-DESTDIR.patch
URL:		http://user.cs.tu-berlin.de/~schintke/x2html/index.html
BuildRequires:	flex, autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C2html highlights C-language sources like emacs does. Output is in
html format. Also works as CGI to convert files on the fly.

%description -l pl
C2html pod¶wietla sk³adniê ¼róde³ C podobnie jak emacs. Wyj¶cie jest w
formacie html. Dzia³a tak¿e jak CGI konwertuj±c pliki w locie.

%prep
%setup -q
%patch0 -p0

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# to aviod "warning: found installed files not placed in any package: blabla
rm -f $RPM_BUILD_ROOT/usr/doc/c2html/{AUTHORS,COPYING,NEWS,README,c2html.lsm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README c2html.lsm
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
