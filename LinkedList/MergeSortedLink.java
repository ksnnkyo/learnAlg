import java.util.*;

public class MergeSortedLink {

    static class ListNode {
        int val;
        ListNode next = null;

        ListNode(int val) {
            this.val = val;
        }
    }

    public static ListNode stringToList(String[] linkNodes) {
        ListNode firstNode = new ListNode(Integer.parseInt(linkNodes[0]));
        ListNode currentNode = firstNode;
        for (int i = 1; i < linkNodes.length; i++) {
            ListNode nextNode = new ListNode(Integer.parseInt(linkNodes[i]));
            currentNode.next = nextNode;
            currentNode = nextNode;
        }
        return firstNode;
    }

    public static String nodeToString(ListNode node) {
        ArrayList<String> nodes = new ArrayList<>();
        ListNode tempNode = node;
        while (tempNode != null) {
            nodes.add(tempNode.val + "");
            tempNode = tempNode.next;
        }
        return String.join("->", nodes);
    }

    public static void main(String args[]) {
        String strIn = "1->3->5,2->4->6->8";
        String firstLink = strIn.split(",")[0];
        String secondLink = strIn.split(",")[1];
        String[] firstLinkNodes = firstLink.split("->");
        ListNode firstNode = stringToList(firstLinkNodes);
        System.out.println(nodeToString(firstNode));
        String[] secondLinkNodes = secondLink.split("->");
        ListNode secondNode = stringToList(secondLinkNodes);
        System.out.println(nodeToString(secondNode));

        ListNode headNode = null;
        if (firstNode.val < secondNode.val) {
            headNode = firstNode;
            firstNode = firstNode.next;
        } else {
            headNode = secondNode;
            secondNode = secondNode.next;
        }
        ListNode currentNode = headNode;
        while (firstNode != null && secondNode != null) {

            if (firstNode.val <= secondNode.val) {
                currentNode.next = firstNode;
                firstNode = firstNode.next;
            } else {
                currentNode.next = secondNode;
                secondNode = secondNode.next;
            }
            currentNode = currentNode.next;
        }
        if (firstNode == null) {
            currentNode.next = secondNode;
        } else {
            currentNode.next = firstNode;
        }

        System.out.println(nodeToString(headNode));
    }
}