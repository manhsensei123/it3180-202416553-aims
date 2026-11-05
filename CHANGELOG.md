# Changelog

Mọi thay đổi đáng chú ý của dự án AIMS-mini đều được ghi nhận tại tệp này.

## [Unreleased]

## [1.1.0] - 2026-11-05

### Added

- Chức năng tìm kiếm đĩa DVD theo thể loại `search_by_category()`.
- Chức năng sắp xếp giỏ hàng `Cart.sort_by_title()` và `Cart.sort_by_cost()`.

## [1.0.1] - 2026-11-05

### Fixed

- Sửa lỗi `search_by_title()` phân biệt chữ hoa/thường (#21)

## [1.0.0] - 2026-11-05

### Added

- Cấu trúc gói `aims` với `DigitalVideoDisc` và `Cart`.
- Chức năng `print_cart()`, `total_cost_with_discount()`, `search_by_title()`.

### Fixed

- Sửa lỗi giới hạn giỏ hàng cho phép thêm đĩa thứ 21 vượt quá `MAX_NUMBERS_ORDERED`.
- Sửa công thức tính tiền sau giảm giá và kiểm tra giá trị phần trăm hợp lệ.
