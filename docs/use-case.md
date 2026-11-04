# Đặc tả Use Case – AIMS-mini

```mermaid
flowchart LR
    Customer([Khách hàng])
    UC1(Thêm đĩa DVD vào giỏ hàng)
    UC2(Xóa đĩa DVD khỏi giỏ hàng)
    UC3(Xem chi tiết giỏ hàng & tổng tiền)
    UC4(Tìm kiếm đĩa DVD theo tiêu đề)

    Customer --> UC1
    Customer --> UC2
    Customer --> UC3
    Customer --> UC4
## Mô tả tóm tắt

1. **Thêm đĩa DVD (`add_dvd`):** Thêm đĩa vào giỏ nếu số lượng chưa vượt giới hạn 20 đĩa.
2. **Xóa đĩa DVD (`remove_dvd`):** Loại bỏ đĩa khỏi giỏ hàng hiện tại.
3. **Hiển thị giỏ hàng (`print_cart`):** Liệt kê danh sách đĩa, đơn giá và tổng chi phí.
4. **Tìm kiếm theo tiêu đề (`search_by_title`):** Lọc các đĩa DVD chứa từ khóa trong tiêu đề.
```
