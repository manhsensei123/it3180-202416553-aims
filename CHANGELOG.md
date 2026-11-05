# Changelog

Mọi thay đổi đáng chú ý của dự án AIMS-mini đều được ghi nhận tại tệp này.

## [Unreleased]

## [1.0.0] - 2026-11-05
### Added
- Tổ chức mã nguồn thành package `aims` gồm `DigitalVideoDisc` và `Cart`.
- Thêm chức năng in chi tiết giỏ hàng `Cart.print_cart()` (có xử lý giỏ hàng trống).
- Thêm chức năng tìm kiếm đĩa DVD theo tiêu đề `search_by_title()`.
- Thêm chức năng tính tổng tiền sau giảm giá `Cart.total_cost_with_discount()`.
- Bổ sung tài liệu đặc tả Use Case (`docs/use-case.md`) và mẫu Pull Request template.

### Fixed
- Sửa lỗi giới hạn giỏ hàng cho phép thêm đĩa thứ 21 vượt quá `MAX_NUMBERS_ORDERED` (#7).
- Sửa công thức tính tiền sau giảm giá và kiểm tra giá trị phần trăm hợp lệ trong đoạn `[0, 100]`.
