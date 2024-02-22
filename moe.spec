Summary:	Powerful and user-friendly text editor
Summary(pl.UTF-8):	Funkcjonalny i przyjazny edytor tekstu
Name:		moe
Version:	1.14
Release:	1
License:	GPL v2+
Group:		Applications/Editors
Source0:	https://ftp.gnu.org/gnu/moe/%{name}-%{version}.tar.lz
# Source0-md5:	d8bbcdfac39afedcd5baf430af310ef6
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/moe/
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	lzip
BuildRequires:	ncurses-devel >= 5.6
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU moe is a powerful, 8-bit clean, console text editor for ISO-8859-15
and ASCII character encodings. It has a modeless, user-friendly
interface, online help, multiple windows, unlimited undo/redo
capability, unlimited line length, unlimited buffers, global
search/replace (on all buffers at once), block operations, automatic
indentation, word wrapping, file name completion, directory browser,
duplicate removal from prompt histories, delimiter matching, text
conversion from/to UTF-8, romanization, etc.

%description -l pl.UTF-8
GNU moe to funkcjonalny konsolowy edytor tekstu, obsługujący kodowania
8-bitowe ISO-8859-15 i ASCII. Ma przyjazny interfejs użytkownika bez
różnych trybów, pomoc online, wiele okien, nieograniczone undo/redo,
nieograniczoną długość linii, nieograniczone bufory, globalne funkcje
znajdź/zastąp (na wszystkich buforach jednocześnie), operacje blokowe,
automatyczne wcięcia, zawijanie słów, dopełnianie nazw plików,
przeglądarkę katalogów, usuwanie duplikatów z historii, dopasowywanie
ograniczników, konwersję tekstu z/do UTF-8, sprowadzanie do alfabetu
łacińskiego itp.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/moe
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/moe.conf
%{_mandir}/man1/moe.1*
%{_infodir}/moe.info*
