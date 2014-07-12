Summary:	Search and display ISO codes for countries, languages, currencies and scripts
Summary(pl.UTF-8):	Wyszukiwanie i wyświetlanie kodów ISO krajów, języków, walut i pism
Name:		isoquery
Version:	2.0
Release:	1
License:	GPL v3+
Group:		Applications
Source0:	http://pkg-isocodes.alioth.debian.org/downloads/%{name}-%{version}.tar.xz
# Source0-md5:	139ecd2b2e47d742d2c5889e41292054
URL:		http://pkg-isocodes.alioth.debian.org/
# rst2man
BuildRequires:	docutils
BuildRequires:	gettext-devel >= 0.18
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libisocodes-devel >= 1.2
BuildRequires:	po4a
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.20
BuildRequires:	xz
Requires:	iso-codes >= 3.52
Requires:	libisocodes >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Search and display ISO codes for countries, languages, currencies and
scripts.

%description -l pl.UTF-8
Wyszukiwanie i wyświetlanie kodów ISO krajów, języków, walut i pism.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/isoquery
%{_mandir}/man1/isoquery.1*
%lang(de) %{_mandir}/de/man1/isoquery.1*
%lang(fr) %{_mandir}/fr/man1/isoquery.1*
%lang(pt) %{_mandir}/pt/man1/isoquery.1*
